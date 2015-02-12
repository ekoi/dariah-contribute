from django import forms

from .models import AnnualValue

class AnnualValueForm(forms.ModelForm):
    required_css_class = 'required'
    #inkind = forms.ModelChoiceField(queryset=AnnualValue.objects.all(), empty_label="Choose one of my contributions below:", help_text="Inkind help text")
    justification = forms.CharField( widget=forms.Textarea, help_text="Help text for 'justification'- forms.py")
   
    class Meta:
        model = AnnualValue
        
    