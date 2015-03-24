from django import forms

from .models import Person

class PersonForm(forms.ModelForm):
    required_css_class = 'required'
    
    class Meta:
        model = Person
        
    