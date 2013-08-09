# hi
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, check_password
# import fastpass

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255) # you probably want this to be an FK to another model

    def __unicode__(self):
        return self.title

class BookList(models.Model):
    title = models.FileField(upload_to='documents/%Y/%m/%d')
    user = models.ForeignKey(User, related_name="booklists") # imported from django.contrib.auth.models
    books = models.ManyToManyField(Book, related_name="lists")

    def __unicode__(self):
        return self.books

class AdminAccount(models.Model):
    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'admin'

class Bookie(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)

    # identifier = models.CharField(max_length=40, unique=True, db_index=True)
    USERNAME_FIELD = 'identifier'
    booklist = models.ForeignKey(BookList, null=True, blank=True)

    def __unicode__(self):
        return self.name

# create user object to attach to Bookie object
# def create_bookie_callback(sender, instance, **kwargs):
#     bookie.new = Bookie.objects.get_or_create(user=instance)
# post_save.connect(create_bookie_callback, User)