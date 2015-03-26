from django import forms

from .models import AnnualValue

class AnnualValueForm(forms.ModelForm):
    required_css_class = 'required'
    
    class Meta:
        model = AnnualValue
    