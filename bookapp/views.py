# Hi

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.conf import settings
from .forms import BookForm
import requests
from django.urls import reverse
from fuzzywuzzy import fuzz
from bookapp.forms import RegistrationForm, LoginForm
from bookapp.models import Bookie
# import fastpass 
import gspread
import sys
import urllib.parse
from .library import get_library_details

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
    gr_rating = 0
    checked_in_books = []
    for book_title, author in booklist:
        details = get_details(book_title, author, lib_location, None)  # library_base_url not needed anymore
        if details:
            checked_in_books.append(details)
            print("processed!")

    sorry_msg = """
    Sorry, no amount of fairy dust can check in 
    any of these books for you. Check back again in a few days.
    """
    return render(
        request,'booklist.html', 
        { 'booklist': checked_in_books }
        )

def get_details(book, author, library):
    details = get_library_details(book, author, library)
    if not details:
        return None
    title = details[0]
    library_author = details[1]
    #rating = find_gr_ratings(create_gr_url(book))
    rating = "ratings not found"
    return (title, rating)
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