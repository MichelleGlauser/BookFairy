from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from forms import UploadFileForm
# , 
from pyquery import PyQuery as pq
import requests
from django.template import RequestContext
from django.core.urlresolvers import reverse

#? instead of line 3?
import models #or, from myproject.myapp.models import Book, BookList
import forms # or, from myproject.myapp.forms import BookForm, UploadFileForm
#import settings?

# def enter_search(request):
#     # Code to lookup book availability
#     form = BookForm() # An unbound form
#     #other option for a message that they've submitted nothing? 
#     return render(request, 'index.html', {'form': form})

# def check_books(request):
#     form = BookForm(request.POST) # A form bound to the POST data
#     if form.is_valid(): # All validation rules pass
#         # Process the data in form.cleaned_data
#         # print "in is_valid"
#         book_info = form.cleaned_data['book_info']
#         print book_info
#         # Get correct site for book title and author
#         # is_checked_in = True
#         base_url = create_url(book_info)
#         return render(request, 'booklist.html', { 'book_info': book_info, 'is_checked_in': check_if_in(base_url) })
#         return HttpResponseRedirect('/booklist')
#         #return render(request, 'index.html')
#         return HttpResponse("Hello, world. You're at the book fairy.")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_info = form.cleaned_data['book_info'] #? Just copied from above
            handle_uploaded_file(request.FILES['file'])

            # new_booklist = BookList(request.FILES['file']) #Or 'docfile'?
            # new_booklist.save()

            return HttpResponseRedirect('/booklist')
    else:
        form = UploadFileForm()
    # c = {'form':form}
    # c.update(csrf(request))

    return render('index.html', {'form': form},
        context_instance=RequestContext(request))




def handle_uploaded_file(file):
    with open('file.name', 'wb+') as destination: #how do I put the name of the uploaded file here?
        #why is this function being called when I do a book search and not a list search?
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()

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
    print base_url

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
    return render(request,'booklist.html')

