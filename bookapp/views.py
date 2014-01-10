# Hi

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from forms import BookForm
from pyquery import PyQuery as pq
import requests
from django.template import RequestContext
from django.core.urlresolvers import reverse
from fuzzywuzzy import fuzz
from bookapp.forms import RegistrationForm, LoginForm
from bookapp.models import Bookie
# import fastpass 
import gspread

def registration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('profile/')

    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        bookie = Bookie.objects.create(
            user=user,
            name=form.cleaned_data['name'],
            # figure out how to get email
        )
        return HttpResponseRedirect('/profile/')
    return render_to_response(
        'register.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def show_profile(request):
    return render_to_response(
        'profile.html',
        context_instance=RequestContext(request)
    )


# authenticate users
def register_user(request):
    pass


# log in users
def let_user_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
        #redirect to a success page.
        else:
            # Return a 'disabled account' error message
            print "This account has been disabled."
    else:
        # Return an 'invalid login' error message.
        pass


def kick_user_out(request):
    logout(request)
    #redirect to a success page


# BOOKLIST UPLOADING
def process_book_file(book_file):
    booklist = []
    for line in book_file:
        comma_index = line.rfind(",")
        if comma_index != -1:
            title = line[:comma_index].strip()
            author = line[comma_index + 1:].strip()
            booklist.append((title, author))
    print booklist
    return booklist


# LIBRARY SEARCHING
# to retrieve the SFPL site url for any book
def create_library_url(search_query, lib_location = "3"):
    #PROMPT
    #MAIN LIBRARY. THIS WILL CHANGE WHEN I ALLOW OTHER INPUT.
    #MAKES TITLE AND AUTHOR (SEARCH QUERY) WORK IN A URL
    joined_query = "+".join(search_query.split())
    #SETTING UP COMPONENTS OF SEARCH URL 
    # searchscope=library location
    # m=media type (a=book)
    list = ["?SEARCH=", joined_query, "&x=0&y=0&searchscope=", lib_location, "&p=&l=eng&m=a&Da=&Db=&SORT=D&availlim=1"]
    #START OF THE URL
    library_base_url = "http://sflib1.sfpl.org/search/X"

    # STICK THE PARTS TOGETHER TO CREATE A URL WITH THE SEARCH
    for item in list:
        library_base_url += item
        print library_base_url
    
    # print "LIB_URL=", library_base_url
    return library_base_url


def extract_details_from_single(pq_data):
    bib_info_list = pq_data("td.bibInfoData")
    if not bib_info_list:
        return None
    title_td = bib_info_list[2]
    title_text = title_td.text_content()

    author_td = bib_info_list[1]
    author_text = author_td.text_content()

    return (title_text, author_text)


def extract_details_from_multiple(book_title, author, pq_data):
    book_trs = pq_data("tr.briefCitRow")

    biblio_info = []
    for book_tr in book_trs:
        query_obj = pq(book_tr)
        title = query_obj("table")[1].getchildren()[0].text_content().strip()
        author = query_obj("table")[1].getchildren()[1].text_content().strip()
        if author:
            biblio_info.append( (title, author) )
    
    if not biblio_info:
        return None

    scored_info = []
    
    for info in biblio_info:
        title_score = fuzz.token_set_ratio(info[0], book_title)
        author_score = fuzz.token_set_ratio(info[1], author)
        total_score = title_score + author_score
        scored_info.append( (total_score, info) )

    scored_info.sort()
    return scored_info[-1][1]


def extract_details(book_title, author, html):
    pq_data = pq(html)
    details = extract_details_from_single(pq_data)
    if not details:
        details = extract_details_from_multiple(book_title, author, pq_data)

    return details


def get_library_details(book, author, library):
    url = create_library_url(book, library)
    response = requests.get(url).content
    details = extract_details(book, author, response)
    return details


def get_details(book, author, library, library_base_url):
    details = get_library_details(book, author, library)
    if not details:
        return None
    title = details[0]
    library_author = details[1]
    rating = find_gr_ratings(create_gr_url(book))
    return (title, rating)


def read_spreadsheet(google_url):
    gc = gspread.login(sys.argv[1], sys.argv[2])
    google_spread = gc.open("Books to Read")
    # print 'after google_spread'
    google_worksheet = google_spread.get_worksheet("To Read")
    col_titles = google_worksheet.col_values(1) # Does gspread do 1 or 0?
    print col_titles

# to retrieve book info -- figure out with "upload_file" function
def check_books(request):
    form = BookForm(request.POST, request.FILES) # A form bound to the POST data
    if not form.is_valid(): # All validation rules pass
        return render(request, "index.html", {"form": form})
    
    # Process the data in form.cleaned_data -- but what about the location data?
    book_file = form.cleaned_data['book_file']
    google_url = form.cleaned_data['google_url']
    lib_location = form.cleaned_data['lib_location']
    if book_file:
        booklist = process_book_file(book_file) # returns list of title and author
    elif google_url:
        print google_url
        booklist = read_spreadsheet(google_url)
    # print "%r"%lib_location 
    gr_rating = 0
    checked_in_books = []
    for book_title, author in booklist:
        library_base_url = create_library_url(book_title, lib_location)
        details = get_details(book_title, author, lib_location, library_base_url)
        if details:
            checked_in_books.append(details)
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



# GOODREADS SEARCHING
# to retrieve the Goodreads site url for any book
def create_gr_url(search_query):
    joined_query = "+".join(search_query.split())
    url_list = [joined_query, "&search_type=books"]
    gr_url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q="
    for item in url_list:
        gr_url += item
    return gr_url


# to compare Goodreads authors and pick the best
def score_gr_details(search_query):
    gr_url = create_gr_url(search_query)
    response = requests.get(url)
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
        title_score = fuzz.token_set_ratio(info[0], book_title)
        author_score = fuzz.token_set_ratio(info[1], author)
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
    url = create_gr_url(search_query)
    rating = find_gr_ratings(gr_url) # call this one twice?
    scored_info = score_gr_details(search_query)
    return rating



# # STEPS:

# upload file, split into title and author
# create a SFPL URL for the title, then request
# check the title against the SFPL search results using fuzzywuzzy
# check the author against the SFPL search results using fuzzywuzzy
# add fuzzywuzzy correlation percentages and return best
# check for availability for highest correlated items
# create the Goodreads URL
# check the title and author against GR search results using fuzzywuzzy
# add fuzzywuzzy correlation percentages and return best
# check for Goodreads rating for highest correlated item
# put checked in books and Goodreads ratings in a list that prints on the page