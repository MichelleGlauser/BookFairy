from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from forms import BookForm
from pyquery import PyQuery as pq
import requests
from django.template import RequestContext
from django.core.urlresolvers import reverse

# to retrieve book info -- is this function still doing something?
def enter_search(request):
    print "Stuff"
    form = BookForm() # An unbound form
    return render(request, "index.html", {"form": form})


# to retrieve book info -- figure out with "upload_file" function
def check_books(request):
    form = BookForm(request.POST, request.FILES) # A form bound to the POST data
    if not form.is_valid(): # All validation rules pass
        return render(request, "index.html", {"form": form})
    
    # Process the data in form.cleaned_data -- but what about the location data?
    book_file = form.cleaned_data['book_file']
    lib_location = form.cleaned_data['lib_location']
    print "%r"%lib_location 
    gr_rating = 0
    booklist = process_book_file(book_file) # returns booklist list
    checked_in_books = []
    for book in booklist:
        library_base_url = create_library_url(book, lib_location)
        if check_if_in(library_base_url) == True:
            gr_url = create_gr_url(book)
            gr_rating = find_gr_rating(gr_url) #returns gr_rating
            checked_in_books.append( (book, gr_rating) )
            # put these in printed booklist in html: 
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
    # 'is_checked_in': check_if_in(base_url) 

        # return render_to_response('booklist.html', { 'booklist': booklist, 'is_checked_in': check_if_in(base_url) },
        #                           context_instance=RequestContext(request))


    # for book in booklist[1:]:
    #     is_checked_in = check_if_in(create_library_url(book))
    #     if is_checked_in == True:
    #         booklist.append(book)
    #     else:
    #         None
    # sorry_msg = """
    # Sorry, no amount of fairy dust can check in 
    # any of these books for you. Check back again in a few days.
    # """
    # if len(booklist) == 0:

    #     print sorry_msg            
    # file.close()            
    # return render_to_response('booklist.html', { 'is_checked_in': is_checked_in, 'sorry_msg': sorry_msg },
    #                       context_instance=RequestContext(request))
#     else:
#         form = UploadFileForm()

#     return render_to_response('index.html', {'form': form},
#         context_instance=RequestContext(request))

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
    list = ["?SEARCH=", joined_query, "&x=0&y=0&searchscope=", lib_location, "&p=&m=a&Da=&Db=&SORT=D"]
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
    availability = requests.get(fullURL)
    # returns True if the content on the site, 
    # shows the words "CHECK SHELF"
    return "CHECK SHELF" in availability.content 


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
    return gr_rating