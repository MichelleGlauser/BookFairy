from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from forms import BookForm
from pyquery import PyQuery as pq
import requests
from django.template import RequestContext
from django.core.urlresolvers import reverse
from fuzzywuzzy import fuzz

# to retrieve book info -- is this function still doing something?
def enter_search(request):
    # print "Stuff"
    form = BookForm() # An unbound form
    return render(request, "index.html", {"form": form})

def extract_title_from_single(pq_data):
    bib_info_list = pq_data("td.bibInfoData")
    if not bib_info_list:
        return None
    title_td = bib_info_list[2]
    return title_td.text_content()

def extract_title_from_multiple(book_title, pq_data):
    a_tags = pq_data("tr.briefCitRow tr:first-child>td>a")
    
    # print a_tags
    # filtered_tags = []
    # for tag in a_tags:
    #     if tag != "":
    #         filtered_tags.append(tag)

    filtered_tags = [ tag.text for tag in a_tags if tag.text ]
    # print filtered_tags
    scored_tags = []
    for tag in filtered_tags:
        # print tag.text, book_title
        score = fuzz.token_set_ratio(book_title, tag)
        score_pair = (score, tag)
        if score > 50:
            scored_tags.append(score_pair)

    # Other way to write it:
    # scored_tags = [ (fuzz.token_set_ratio(title, tag), tag) 
    #                     for tag in filtered_tags ]

    scored_tags.sort()
    if not scored_tags:
        return None

    best = scored_tags[-1]
    return best[1]


def extract_title(book_title, html):
    pq_data = pq(html)
    title = extract_title_from_single(pq_data)
    if not title:
        title = extract_title_from_multiple(book_title, pq_data)

    return title


def get_library_title(book, library):
    url = create_library_url(book, library)
    response = requests.get(url).content
    title = extract_title(book, response)
    return title

def get_details(book, library):
    title = get_library_title(book, library)
    if not title:
        return None
    rating = get_goodreads_rating(book)
    return (title, rating)

# to retrieve book info -- figure out with "upload_file" function
def check_books(request):
    form = BookForm(request.POST, request.FILES) # A form bound to the POST data
    if not form.is_valid(): # All validation rules pass
        return render(request, "index.html", {"form": form})
    
    # Process the data in form.cleaned_data -- but what about the location data?
    book_file = form.cleaned_data['book_file']
    lib_location = form.cleaned_data['lib_location']
    # print "%r"%lib_location 
    gr_rating = 0
    booklist = process_book_file(book_file) # returns booklist list
    checked_in_books = []
    for book in booklist:
        details = get_details(book, lib_location)
        if details:
            checked_in_books.append(details)
        # library_base_url = create_library_url(book, lib_location)
        # if check_if_in(library_base_url) == True:
        #     gr_url = create_gr_url(book)
        #     gr_rating = find_gr_rating(gr_url) #returns gr_rating
        #     checked_in_books.append( (book, gr_rating) )
        #     # put these in printed booklist in html: 
            # {{ booklist }}, {{ gr_rating }}
            # HOW? THE RATINGS NEED TO BE ASSIGNED! 
            # booklist = iter(booklist) # says needs 2 length
            # booklist_dict = dict(zip(booklist, ))
            # b = dict(zip(i, i))
            print "processed!"
    # print booklist
    sorry_msg = """
    Sorry, no amount of fairy dust can check in 
    any of these books for you. Check back again in a few days.
    """
    return render(
        request,'booklist.html', 
        { 'booklist': checked_in_books }
        )

# opens book file and puts the books in a list
def process_book_file(book_file):
    booklist = []
    for line in book_file:
        # add books to a list
        booklist.append(line)
        # print book_titles
    booklist[0].split('\r')
    return booklist


# to retrieve the SFPL site url for any book
def create_library_url(search_query, lib_location = "3"):
    #PROMPT
    #MAIN LIBRARY. THIS WILL CHANGE WHEN I ALLOW OTHER INPUT.
    #MAKES TITLE AND AUTHOR (SEARCH QUERY) WORK IN A URL
    joined_query = "+".join(search_query.split())
    #SETTING UP COMPONENTS OF SEARCH URL 
    # searchscope=library location
    # m=media type (a=book)
    list = ["?SEARCH=", joined_query, "&x=0&y=0&searchscope=", lib_location, "&p=&m=a&Da=&Db=&SORT=D&availlim=1"]
    #START OF THE URL
    library_base_url = "http://sflib1.sfpl.org/search/X"

    # STICK THE PARTS TOGETHER TO CREATE A URL WITH THE SEARCH
    for item in list:
        library_base_url += item
    
    # print "LIB_URL=", library_base_url
    return library_base_url

# to see if the book is checked in
def check_if_in(library_base_url):
    # retrieves created URL
    response = requests.get(library_base_url)
    # gets the content from the created URL
    pyed_data = pq(response.content)
    # print pyed_data
    detail = pyed_data("p.detail").eq(0) #shows whole p class
    print "DETAIL=", detail
    area = pyed_data(detail).children("a") # looks like this does the same thing
    print "AREA=", area
    href = pyed_data(area).attr("href") # this provides the URL without any tags
    print href
    fullURL = "http://sflib1.sfpl.org" + href
    # if href is None:
         
    availability = requests.get(fullURL)
    # returns True if the content on the site, 
    # shows the words "CHECK SHELF"
    return "CHECK SHELF" in availability.content 


def get_goodreads_rating(book):
    url = create_gr_url(book)
    rating = find_gr_ratings(url)
    return rating

# to retrieve the Goodreads site url for any book
def create_gr_url(gr_search_query):
    joined_query = "+".join(gr_search_query.split())
    url_list = [joined_query, "&search_type=books"]
    #START OF THE URL
    gr_url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q="

    # STICK THE PARTS TOGETHER TO CREATE A URL WITH THE SEARCH
    for item in url_list:
        gr_url += item
    return gr_url


# to retrieve the Goodreads rating 
def find_gr_ratings(gr_url):
    url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books"
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

# to retrieve the Goodreads rating 
# def find_gr_ratings(gr_url):
#     # example_url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=atlas+shrugged+ayn+rand&search_type=books"
#     # requests gr_url 
#     response = requests.get(gr_url)
#     # retrieves content from gr_url
#     data = pq(response.content)

#     books = data("tr[itemtype='http://schema.org/Book']")

#     # gets to the correct area of html
#     area = data("span.minirating").eq(0)
#     a_info = data(b).children("td").eq(1) ??
#     b_info = data(a_info).children("a.bookTitle")
    
#     a = data(area)
#     # pulls out rating avg and number of ratings
#     gr_ratings = a.text()
#     return gr_ratings



# def filter_gr_ratings(gr_ratings):
#     get title and author using pyquery 
#     put title and author into lists and use fuzzywuzzy to rate
#     sort lists
#     how to connect the lists?
#     choose book with highest correlation between search and title and author
#     put rating into the list to be put on the booklist page
