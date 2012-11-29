from django import forms

class BookForm(forms.Form):
    book_file = forms.FileField( #shows the choose file
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
        ],

        label="Library Branch")

#       <option value="8"> Chinatown</option> 
#       <option value="9"> Eureka Valley</option> 
#       <option value="10"> Excelsior</option> 
#       <option value="11"> Glen Park</option> 
#       <option value="12"> Golden Gate Valley</option> 
#       <option value="13"> Ingleside</option> 
#       <option value="14"> Library on Wheels</option> 
#       <option value="3"> Main Library</option> 
#       <option value="15"> Marina</option> 
#       <option value="16"> Merced</option> 
#       <option value="17"> Mission</option> 
#       <option value="18"> Mission Bay</option> 
#       <option value="19"> Noe Valley</option> 
#       <option value="20"> North Beach</option> 
#       <option value="21"> Oceanview</option> 
#       <option value="22"> Ortega</option> 
#       <option value="23"> Park</option> 
#       <option value="24"> Parkside</option> 
#       <option value="25"> Portola</option> 
#       <option value="26"> Potrero</option> 
#       <option value="27"> Presidio</option> 
#       <option value="28"> Richmond</option> 
#       <option value="29"> Sunset</option> 
#       <option value="30"> Visitacion Valley</option> 
#       <option value="31"> West Portal</option> 
#       <option value="34"> Western Addition</option> 
