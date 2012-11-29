book_titles = ['Title,Author\rThe Hobbit,Tolkien\rA Tree Grows in Brooklyn,Betty Smith\rProgramming Interviews Exposed,Mongan\rAtlas Shrugged ,Ayn Rand\rTheir Eyes Were Watching God,Zora Neale Hurston'] 
print book_titles

def strip_booklist():
    for book in book_titles[1:]:
        book = book.strip
        print book