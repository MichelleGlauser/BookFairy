from django import forms

class BookForm(forms.Form):
    book_file = forms.FileField(  # shows the choose file
        label="Select a file:",
        help_text='max. 42 megabytes')
    lib_location = forms.ChoiceField(
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
