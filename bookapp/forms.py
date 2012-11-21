from django import forms

class BookForm(forms.Form):
    book_info = forms.CharField(max_length=200, label="Book Title and Author:")
    # title = forms.CharField(max_length=50, label="File:") #shows the text field
    file = forms.FileField() #shows the choose file
    #How do I combine the title and file fields so that a box shows up, but you can choose as well?

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50, label="File:")
#     file = forms.FileField()

    def __unicode__(self):
        return self.title