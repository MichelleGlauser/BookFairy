import requests
from pyquery import PyQuery as pq
from fuzzywuzzy import fuzz
from pprint import pprint

import urllib

# GOODREADS SEARCHING
# to retrieve the Goodreads site url for any book
def get_gr_search_url(title, author):
    base_url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q="
    return f"{base_url}{title} {author}&search_type=books"

user_agent = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}
# to compare Goodreads authors and pick the best
def find_gr_rating(title, author):
    try:
        gr_url = get_gr_search_url(title, author)
        response = requests.get(gr_url, headers=user_agent, timeout=6.1)
        pq_data = pq(response.content)
        books = pq_data("tr[itemtype='http://schema.org/Book']")
        all_info = books.children("td").eq(1)
        
        biblio_info = []
        for row in all_info.items():
            title_el = row.find("a.bookTitle")
            author_el = row.find("a.authorName")
            rating_el = row.find("span.minirating")
            if len(title_el) == 0 or len(author_el) == 0 or len(rating_el) == 0:
                continue
            title = title_el.text().strip()
            author = author_el.text().strip()
            rating = float(rating_el.text().strip().partition(" ")[0])
            if title and author and rating:
                biblio_info.append((title, author, rating))
        if not biblio_info:
            print(all_info.contents())
            return None

        def score(info):
            title_score = fuzz.token_set_ratio(info[0], title)
            author_score = fuzz.token_set_ratio(info[1], author)
            return title_score + author_score

        return max(biblio_info, key=score)[2]
    except Exception as e:
        print(f"Error fetching Goodreads rating: {e}")
        return None
