from django.contrib import admin
from models import Book, BookList

class BookappAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookappAdmin)
admin.site.register(BookList, BookappAdmin)