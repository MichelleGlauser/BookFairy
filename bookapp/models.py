from django.db import models
from django.contrib.auth.models import User
from django import forms

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255) # you probably want this to be an FK to another model

    def __unicode__(self):
        return self.title

class BookList(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name="booklists") # imported from django.contrib.auth.models
    books = models.ManyToManyField(Book, related_name="lists")

