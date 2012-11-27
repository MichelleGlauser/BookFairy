from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from forms import BookForm, UploadFileForm
from pyquery import PyQuery as pq
import requests
from django.template import RequestContext
from django.core.urlresolvers import reverse

def enter_search(request):
    # Code to lookup book availability
    form = BookForm() # An unbound form
    #other option for a message that they've submitted nothing? 
    return render_to_response(request, 'index.html', {'form': form})

def check_books(request):
    form = BookForm(request.POST) # A form bound to the POST data
    if form.is_valid(): # All validation rules pass
        # Process the data in form.cleaned_data
        # print "in is_valid"
        book_info = form.cleaned_data['book_info']
        print book_info
        # Get correct site for book title and author
        # is_checked_in = True
        base_url = create_url(book_info)
        return render_to_response('booklist.html', { 'book_info': book_info, 'is_checked_in': check_if_in(base_url) },
                                  context_instance=RequestContext(request))

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
                is_checked_in = check_if_in(create_url(book))
                if is_checked_in == True:
                    booklist.append(book)
                else:
                    sorry_msg = """
                    Sorry, no amount of fairy dust can check in 
                    any of these books for you. Check back again in a few days.
                    """
                    print sorry_msg 
                    
            # here is where you'll want to parse the comma delimited file and
            # check each book
            
            file.close()            
            return render_to_response('booklist.html', { 'booklist': booklist },
                                  context_instance=RequestContext(request))
    else:
        form = UploadFileForm()

    return render_to_response('index.html', {'form': form},
        context_instance=RequestContext(request))


def create_url(search_query):
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
    base_url = "http://sflib1.sfpl.org/search/X"

    # STICK THE PARTS TOGETHER TO CREATE A URL WITH THE SEARCH
    for item in list:
        base_url += item
    
    return base_url

# See if the book is checked in.
def check_if_in(base_url):
    # retrieves created URL
    response = requests.get(base_url)
    # gets the content from the created URL
    pyed_data = pq(response.content)
    # useless?
    # pyed_data =("p.detail")
    detail = pyed_data("p.detail").eq(0)
    area = pyed_data(detail).children("a")
    pyed_data(area).attr("href")
    href = pyed_data(area).attr("href")
    fullURL = "http://sflib1.sfpl.org" + href
    print fullURL
    availability = requests.get(fullURL)
    return "CHECK SHELF" in availability.content 

def booklist(request):
    # book_info = 
    # post to booklist page
    return render_to_response(request,'booklist.html')

