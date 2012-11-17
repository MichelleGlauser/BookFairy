from django import forms

class BookForm(forms.Form):
    book_info = forms.CharField(max_length=200, label="Book Title and Author:")
