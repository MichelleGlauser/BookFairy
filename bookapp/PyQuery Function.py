url = "http://www.goodreads.com/search?utf8=%E2%9C%93&q=Their+Eyes+Were+Watching+God+Zora+Neale+Hurston&search_type=books&auto_login_attempted=true"

def filter_gr_ratings(url):
    response = requests.get(url)
    pqd = pq(response.content)
    books = pqd("tr[itemtype='http://schema.org/Book']")
    booklist = []
 
    for book in books:
        book_dict = {}
        all_info = pqd(book).children("td").eq(1)
        
        book_info = pqd(all_info).children("a.bookTitle")
        book_dict['title'] = pqd(book_info).text()
 
        author_info = pqd(all_info).find("a.authorName")                                                                                                                                                                                      
        book_dict['author'] = pqd(author_info).text()

        booklist.append(book_dict)
 
    return booklist
 
filter_gr_ratings(url)



# URL to author page, DON'T NEED
    # book_dict['authorURL'] = pqd(author_info).attr("href")
# SHOWS LINK, DON'T NEED
# book_dict['bookURL'] = pqd(book_info).attr("href")