# Hi

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.conf import settings
from .forms import BookForm
from pyquery import PyQuery as pq
import requests
from django.urls import reverse
from fuzzywuzzy import fuzz
from bookapp.forms import RegistrationForm, LoginForm
from bookapp.models import Bookie
# import fastpass 
import gspread
import sys
import urllib.parse
import xml.etree.ElementTree as ET

def enter_search(request):
    """Main page view that displays the book search form."""
    form = BookForm()
    return render(request, 'index.html', {'form': form})

def login(request):
    """Login view for user authentication."""
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth_login(request, user)
            return HttpResponseRedirect('/profile/')
        else:
            form.add_error(None, 'Invalid username or password.')
    
    return render(request, 'login.html', {'form': form})

def registration(request):
    if request.user.is_authenticated:
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
    return render(
        request,
        'register.html',
        {'form': form}
    )

def show_profile(request):
    return render(
        request,
        'profile.html'
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
            print("This account has been disabled.")
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
        # Decode bytes to string if necessary
        if isinstance(line, bytes):
            line = line.decode('utf-8')
        line = line.strip()  # Remove any trailing newlines/whitespace
        comma_index = line.rfind(",")
        if comma_index != -1:
            title = line[:comma_index].strip()
            author = line[comma_index + 1:].strip()
            booklist.append((title, author))
    print(booklist)
    return booklist


# LIBRARY SEARCHING
# to retrieve the SFPL site url for any book using the new BiblioCommons API
def create_library_url(book_title, author, lib_location="3"):
    """
    Create a BiblioCommons RSS search URL for SFPL
    lib_location mapping to branch names needs to be updated
    """
    
    # Map location codes to exact branch names as used by the new API
    location_map = {
        "3": "MAIN",
        "4": "ANZA BRANCH",
        "5": "BAYVIEW BRANCH", 
        "6": "BERNAL HEIGHTS BRANCH",
        "8": "CHINATOWN BRANCH",
        "9": "EUREKA VALLEY BRANCH",
        "10": "EXCELSIOR BRANCH",
        "11": "GLEN PARK BRANCH",
        "12": "GOLDEN GATE VALLEY BRANCH",
        "13": "INGLESIDE BRANCH",
        "14": "CHILDREN'S BOOKMOBILE",  # Updated from "Library on Wheels"
        "15": "MARINA BRANCH",
        "16": "MERCED BRANCH",
        "17": "MISSION BRANCH",
        "18": "MISSION BAY BRANCH",
        "19": "NOE VALLEY BRANCH",
        "20": "NORTH BEACH BRANCH",
        "21": "OCEAN VIEW BRANCH",
        "22": "ORTEGA BRANCH",
        "23": "PARK BRANCH",
        "24": "PARKSIDE BRANCH",
        "25": "PORTOLA BRANCH",
        "26": "POTRERO BRANCH",
        "27": "PRESIDIO BRANCH",
        "28": "RICHMOND BRANCH",
        "29": "SUNSET BRANCH",
        "30": "VISITACION VALLEY BRANCH",
        "31": "WEST PORTAL BRANCH",
        "34": "WESTERN ADDITION BRANCH",
    }
    
    branch_name = location_map.get(lib_location, "MAIN")
    
    # Create the search query in the new format
    # Format: title:(Book Title) AND contributor:(Author Name) AND format:(bk) AND avlocation:"BRANCH NAME"
    query = f'title:({book_title}) AND contributor:({author}) AND format:(bk) AND avlocation:"{branch_name}"'
    
    # URL encode the query
    encoded_query = urllib.parse.quote(query)
    
    # Create the full URL
    base_url = "https://gateway.bibliocommons.com/v2/libraries/sfpl/rss/search"
    full_url = f"{base_url}?query={encoded_query}&searchType=bl"
    
    print(f"Library URL: {full_url}")
    return full_url


def extract_details_from_rss(book_title, author, xml_content):
    """
    Extract book details from BiblioCommons RSS XML response
    """
    from xml.etree.ElementTree import ParseError
    
    try:
        # Parse the XML
        root = ET.fromstring(xml_content)
        
        # Find all items in the RSS feed
        items = root.findall('.//item')
        
        if not items:
            print("No items found in RSS feed")
            return None
        
        # Extract book information from items
        biblio_info = []
        for item in items:
            title_elem = item.find('title')
            creator_elem = item.find('.//{http://purl.org/dc/elements/1.1/}creator')
            
            if title_elem is not None and creator_elem is not None:
                title = title_elem.text.strip() if title_elem.text else ""
                creator = creator_elem.text.strip() if creator_elem.text else ""
                
                if title and creator:
                    biblio_info.append((title, creator))
        
        if not biblio_info:
            print("No valid book info found in RSS items")
            return None
        
        # Use fuzzy matching to find the best match
        scored_info = []
        for info in biblio_info:
            title_score = fuzz.token_set_ratio(info[0], book_title)
            author_score = fuzz.token_set_ratio(info[1], author)
            total_score = title_score + author_score
            scored_info.append((total_score, info))
        
        if scored_info:
            scored_info.sort(reverse=True)  # Sort descending by score
            best_match = scored_info[0][1]  # Get the best match
            print(f"Best match: {best_match} (score: {scored_info[0][0]})")
            return best_match
        
        return None
        
    except ParseError as e:
        print(f"XML parsing error: {e}")
        return None
    except Exception as e:
        print(f"Error extracting details from RSS: {e}")
        return None


def extract_details_from_single(pq_data):
    # This function is now deprecated with the new API
    return None


def extract_details_from_multiple(book_title, author, pq_data):
    # This function is now deprecated with the new API  
    return None


def extract_details(book_title, author, content):
    """
    Main function to extract details from library response
    Now uses RSS XML parsing instead of HTML parsing
    """
    # The content is now XML from RSS feed, not HTML
    return extract_details_from_rss(book_title, author, content)


def get_library_details(book, author, library):
    url = create_library_url(book, author, library)  # Now passes both book and author
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        if not response.content:
            print(f"Empty response from library URL: {url}")
            return None
        details = extract_details(book, author, response.content)
        return details
    except requests.RequestException as e:
        print(f"Error fetching library details for '{book}' by '{author}': {e}")
        return None
    except Exception as e:
        print(f"Error parsing library response for '{book}' by '{author}': {e}")
        return None


def get_details(book, author, library, library_base_url):
    details = get_library_details(book, author, library)
    if not details:
        return None
    title = details[0]
    library_author = details[1]
    #rating = find_gr_ratings(create_gr_url(book))
    rating = "ratings not found"
    return (title, rating)


def read_spreadsheet(google_url):
    gc = gspread.login(sys.argv[1], sys.argv[2])
    google_spread = gc.open("Books to Read")
    # print 'after google_spread'
    google_worksheet = google_spread.get_worksheet("To Read")
    col_titles = google_worksheet.col_values(1) # Does gspread do 1 or 0?
    print(col_titles)

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
        print(google_url)
        booklist = read_spreadsheet(google_url)
    # print "%r"%lib_location 
    gr_rating = 0
    checked_in_books = []
    for book_title, author in booklist:
        details = get_details(book_title, author, lib_location, None)  # library_base_url not needed anymore
        if details:
            checked_in_books.append(details)
            print("processed!")
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
    print("DETAIL=", detail)
    area = pyed_data(detail).children("a") # looks like this does the same thing
    print("AREA=", area)
    href = pyed_data(area).attr("href") # this provides the URL without any tags
    print(href)
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
    url = create_gr_url(search_query)
    rating = find_gr_ratings(url)
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