from django import forms

class BookForm(forms.Form):
    book_info = forms.CharField(max_length=200, label="Book Title and Author:")
    # title = forms.CharField(max_length=50, label="File:") #shows the text field
    file = forms.FileField() #shows the choose file
    #How do I combine the title and file fields so that a box shows up, but you can choose the one you want?

# class UploadFileForm(forms.Form):
#     booklist = forms.FileField(
#         label="Select a file:",
#         help_text='max. 42 megabytes')

    def __unicode__(self):
        return self.title