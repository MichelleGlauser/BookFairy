from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from forms import BookForm
from pyquery import PyQuery as pq
import requests

def enter_search(request):
    # Code to lookup book availability
    form = BookForm() # An unbound form
    #other option for a message that they've submitted nothing? 
    return render(request, 'index.html', {'form': form})

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
        return render(request, 'booklist.html', { 'book_info': book_info, 'is_checked_in': check_if_in(base_url) })
        #return render(request, 'index.html')
        #return HttpResponse("Hello, world. You're at the book fairy.")

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
    print pyed_data
    # useless?
    # pyed_data =("p.detail")
    detail = pyed_data("p.detail").eq(0)
    area = pyed_data(detail).children("a")
    pyed_data(area).attr("href")
    href = pyed_data(area).attr("href")
    fullURL = "http://sflib1.sfpl.org" + href
    availability = requests.get(fullURL)
    return "CHECK SHELF" in availability.content 

def booklist(request):
    # book_info = 
    # post to booklist page
    return render(request,'booklist.html')







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
