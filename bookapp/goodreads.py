import requests
from pyquery import PyQuery as pq
from fuzzywuzzy import fuzz
def find_gr_rating(title, author):
    gr_url = get_gr_search_url(title, author)
    # requests gr_url 
    response = requests.get(gr_url)
    # retrieves content from gr_url
    data = pq(response.content)
    # gets to the correct area of html
    area = data("span.minirating").eq(0)
    a = data(area)
    # pulls out rating avg and number of ratings
    gr_rating = a.text()

# GOODREADS SEARCHING
# to retrieve the Goodreads site url for any book
def get_gr_search_url(title, author):
    base_url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q="
    return f"{base_url}{title} {author}&search_type=books"

# to compare Goodreads authors and pick the best
def score_gr_details(search_query):
    gr_url = get_gr_search_url(search_query)
    response = requests.get(gr_url)
    pq_data = pq(response.content)
    books = pq_data("tr[itemtype='http://schema.org/Book']")
    all_info = pq_data(books).children("td").eq(1)
    book_info = pq_data(all_info).children("a.bookTitle")
    author_info = pq_data(all_info).find("a.authorName").eq(0)
    # will books here

    biblio_info = []
    for book in books: # or is it for book in book_info ?
        # query_obj = pq(book)
        title = pq_data(book_info).text().strip()
        author = pq_data(author_info).text().strip()
        if author:
            biblio_info.append( (title, author) )
    
    if not biblio_info:
        return None

    scored_info = []
    
    for info in biblio_info:
        title_score = fuzz.token_set_ratio(info[0], search_query)
        author_score = fuzz.token_set_ratio(info[1], search_query)
        total_score = title_score + author_score
        scored_info.append( (total_score, info) )

    scored_info.sort()
    return scored_info[-1][1]


# to retrieve the Goodreads rating 
def find_gr_ratings(gr_url):
    # url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books"
    # requests gr_url 
    response = requests.get(gr_url)
    # retrieves content from gr_url
    data = pq(response.content)
    # gets to the correct area of html
    area = data("span.minirating").eq(0)
    a = data(area)
    # pulls out rating avg and number of ratings
    gr_rating = a.text()
    return gr_rating


def get_gr_details(search_query):
    url = get_gr_search_url(search_query)
    rating = find_gr_ratings(url)
    scored_info = score_gr_details(search_query)
    return rating


