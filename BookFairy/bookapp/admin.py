from django.contrib import admin
from models import Book, BookList, Bookie, AdminAccount

class BookappAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookappAdmin, Bookie)
admin.site.register(BookList, BookappAdmin, Bookie)

