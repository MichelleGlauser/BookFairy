from django import forms
from django.contrib.auth.models import 


# creates a form out of the model
from django.forms import ModelForm
from bookie.models import Bookie

class BookForm(forms.Form):
    book_file = forms.FileField(  # shows the choose file
        label="Booklist File:")
    lib_location = forms.ChoiceField(
        label="Library Location:",
        choices = [
        ("4", "Anza"),
        ("5", "Bayview"),
        ("6", "Bernal Heights"),
        ("32", "Branch Bookmobile 1"),
        ("8", "Chinatown"),
        ("9", "Eureka Valley"),
        ("10", "Excelsior"),
        ("11", "Glen Park"),
        ("12", "Golden Gate Valley"),
        ("13", "Ingleside"),
        ("14", "Library on Wheels"),
        ("3", "Main"),
        ("15", "Marina"),
        ("16", "Merced"),
        ("17", "Mission"),
        ("18", "Mission Bay"),
        ("19", "Noe Valley"),
        ("20", "North Beach"),
        ("21", "Oceanview"),
        ("22", "Ortega"),
        ("23", "Park"),
        ("24", "Parkside"),
        ("25", "Portola"),
        ("26", "Potrero"),
        ("27", "Presidio"),
        ("28", "Richmond"),
        ("29", "Sunset"),
        ("30", "Visitacion Valley"),
        ("31", "West Portal"),
        ("34", "Western Addition"),

        ])

class RegistrationForm(ModelForm)
    username = forms.CharField(label=(u'User Name'))
    email = forms.EmailField(label=(u'Email Address'))
    password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False)
    password1 = forms.CharField(label=(u'Verify Password'), widget=froms.PasswordINput(render_value=False))

    class Meta:
        model = Bookie
        exclude = ('user',)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Sorry, that username is already taken.")

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("The passwords did not match. Please try again.")
        return self.cleaned_data

        # password = self.cleaned_data['password']
        # password1 = self.cleaned_data['password1']
        # if password != password1:
        #     raise forms.ValidationError('Your passwords did not match.')
        # return password

class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(label=('u'Password'), widget=forms.PasswordInput(render_value=False))
    