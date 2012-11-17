# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from forms import BookForm
from pyquery import PyQuery as pq
import requests

def index(request):
    # Code to lookup book availability
    if request.method == 'POST': # If the form has been submitted...
        print "in post"
        form = BookForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            print "in is_valid"
            book_info = form.cleaned_data['book_info']
            print book_info
            # TODO: Add code htere to lookup if the book is checked in
            
            # TODO: is the bookchecked in?
            is_checked_in = True
            return render(request, 'booklist.html', { 'book_info': book_info, 'is_checked_in': is_checked_in } )
    else:
        form = BookForm() # An unbound form

    return render(request, 'index.html', {
        'form': form,
    })
    #return render(request, 'index.html')
    #return HttpResponse("Hello, world. You're at the book fairy.")

def booklist(request):
    # book_info = 
    # post to booklist page
    return render(request,'booklist.html')

def create_url():
    #PROMPT
    search_query = raw_input("Book title and author?") 
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

def retrieve_url(base_url):
    response = requests.get(base_url)
    pyed_data = pq(response.content)
    pyed_data =("p.detail")
    detail = pyed_data("p.detail").eq(0)
    area = pyed_data(detail).children("a")
    py_data(area).attr("href")
    href = py_data(area).attr("href")
    fullURL = "http://sflib1.sfpl.org" + href

def checkedin(fullURL):
    availability = requests.get(fullURL)

    if "CHECK SHELF" in availability.content == True:
        print "Checked in!"


# >>> sample_url = "http://sflib1.sfpl.org/search/X?SEARCH=world+war+z&x=46&y=10&searchscope=3&p=&m=a&Da=&Db=&SORT=D"
# >>> base_url = "http://sflib1.sfpl.org/search/X"
# >>> r = requests.get(base_url, params={"SEARCH": "world war z", "searchscope": 3, "m": "a"})
# >>> dom = pq(r.text)
# >>> links = dom("tr.briefCitRow p.detail a")
# >>> print links
# <a href="/search~S3?/Xworld+war+z&amp;searchscope=3&amp;m=a&amp;SORT=D/Xworld+war+z&amp;searchscope=3&amp;m=a&amp;SORT=D&amp;SUBKEY=world+war+z/1%2C43%2C43%2CB/frameset&amp;FF=Xworld+war+z&amp;searchscope=3&amp;m=a&amp;SORT=D&amp;1%2C1%2C"><img src="/screens/isitavailable.gif" alt="Is it available?" border="0"/></a><a href="/search~S3?/Xworld+war+z&amp;searchscope=3&amp;m=a&amp;SORT=D/Xworld+war+z&amp;searchscope=3&amp;m=a&amp;SORT=D&amp;SUBKEY=world+war+z/1%2C43%2C43%2CB/frameset&amp;FF=Xworld+war+z&amp;searchscope=3&amp;m=a&amp;SORT=D&amp;2%2C2%2C"><img 
# links[0].get("href")
# '/search~S3?/Xworld+war+z&searchscope=3&m=a&SORT=D/Xworld+war+z&searchscope=3&m=a&SORT=D&SUBKEY=world+war+z/1%2C43%2C43%2CB/frameset&FF=Xworld+war+z&searchscope=3&m=a&SORT=D&1%2C1%2C'
# >>> new_url = "http://sflib1.sfpl.org" + links[0].get("href") 
# >>> new_url
# 'http://sflib1.sfpl.org/search~S3?/Xworld+war+z&searchscope=3&m=a&SORT=D/Xworld+war+z&searchscope=3&m=a&SORT=D&SUBKEY=world+war+z/1%2C43%2C43%2CB/frameset&FF=Xworld+war+z&searchscope=3&m=a&SORT=D&1%2C1%2C'

#"A Tree Grows in Brooklyn Betty Smith"


#use base_url to search  

# post_request = requests.post(URL)

# URL =furl("http://sflib1.sfpl.org/search/X").add("SEARCH" : search_query).add("x": 36), "y": 10, 
#         "searchscope": location, "p": "", "m": "a", "Da": "", "Db": "", "SORT": "D"}).url 
