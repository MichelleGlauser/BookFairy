# Hi

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# creates a form out of the model
from django.forms import ModelForm
from bookapp.models import Bookie


class BookForm(forms.Form):
    book_file = forms.FileField(  # shows the choose file
        label="Booklist File:", required=False)
    # Do I need these if the Google spreadsheet has open settings?
    # google_user = forms.CharField (label="Google User Name:")
    # google_pass = forms.CharField(label=(u'Google Password'), widget=forms.PasswordInput(render_value=False))
    google_url = forms.URLField (label="Google Drive Spreadsheet URL:", required=False)
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


# from Kenneth Love's advice:
class RegistrationForm(UserCreationForm):
    name = forms.CharField(label="Name")

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False))
    