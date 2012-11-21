from django import forms

class BookForm(forms.Form):
    book_info = forms.CharField(max_length=200, label="Book Title and Author:")


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, label="File:")
    file = forms.FileField()

    def __unicode__(self):
        return self.title