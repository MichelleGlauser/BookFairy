from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from forms import BookForm, UploadFileForm
from pyquery import PyQuery as pq
import requests
from django.template import RequestContext
from django.core.urlresolvers import reverse

# to retrieve book info -- is this function still doing something?
def enter_search(request):

    form = BookForm() # An unbound form
    #other option for a message that they've submitted nothing? 
    return render_to_response(request, 'index.html', {'form': form})


# to retrieve book info -- figure out with "upload_file" function
def check_books(request):
    form = BookForm(request.POST) # A form bound to the POST data
    if form.is_valid(): # All validation rules pass
        # Process the data in form.cleaned_data
        # print "in is_valid"
        book_info = form.cleaned_data['book_info']
        print book_info
        base_url = create_library_url(book_info)
        return render_to_response('booklist.html', { 'book_info': book_info, 'is_checked_in': check_if_in(base_url) },
                                  context_instance=RequestContext(request))

#def choose_library(request):
    # make new form in Forms.py so that user can select a library from a drop-down menu    

# to upload a plain text book list -- split into several views
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['booklist']
            # file = file.split('\r')
            # print file

            book_titles = []

            # since your files are small enough to fit in memory, it's simpler to use
            # read() than splitting the file into chunks
            for line in file:
                # print each line of the file -- for debugging purposes only
                # print line
                # print

                # add books to a list
                book_titles.append(line)
                # print book_titles
            
            booklist = []    
            for book in book_titles[1:]:
                is_checked_in = check_if_in(create_library_url(book))
                if is_checked_in == True:
                    booklist.append(book)
                else:
                    None
            sorry_msg = """
            Sorry, no amount of fairy dust can check in 
            any of these books for you. Check back again in a few days.
            """
            if len(booklist) == 0:

                print sorry_msg
            # here is where you'll want to parse the comma delimited file and
            # check each book
            
            file.close()            
            return render_to_response('booklist.html', { 'is_checked_in': is_checked_in }, { 'sorry_msg': sorry_msg },
                                  context_instance=RequestContext(request))
    else:
        form = UploadFileForm()

    return render_to_response('index.html', {'form': form},
        context_instance=RequestContext(request))


# to retrieve the SFPL site url for any book
def create_library_url(search_query):
    #PROMPT
    #MAIN LIBRARY. THIS WILL CHANGE WHEN I ALLOW OTHER INPUT.
    location = "3"
    #MAKES TITLE AND AUTHOR (SEARCH QUERY) WORK IN A URL
    joined_query = "+".join(search_query.split())
    #SETTING UP COMPONENTS OF SEARCH URL 
    # searchscope=library location
    # m=media type (a=book)
    list = ["?SEARCH=", joined_query, "&x=0&y=0&searchscope=", location, "&p=&m=a&Da=&Db=&SORT=D"]
    #START OF THE URL
    library_base_url = "http://sflib1.sfpl.org/search/X"

    # STICK THE PARTS TOGETHER TO CREATE A URL WITH THE SEARCH
    for item in list:
        library_base_url += item
    
    return library_base_url


# to see if the book is checked in
def check_if_in(library_base_url):
    # retrieves created URL
    response = requests.get(library_base_url)
    # gets the content from the created URL
    pyed_data = pq(response.content)
    detail = pyed_data("p.detail").eq(0) #shows whole p class
    area = pyed_data(detail).children("a") # looks like this does the same thing
    href = pyed_data(area).attr("href") # this provides the URL without any tags
    fullURL = "http://sflib1.sfpl.org" + href 
    print fullURL
    availability = requests.get(fullURL)
    return "CHECK SHELF" in availability.content 


# what is this function for?
def booklist(request):
    # book_info = 
    # post to booklist page
    return render_to_response(request,'booklist.html')

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
def find_gr_rating(gr_url):
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

