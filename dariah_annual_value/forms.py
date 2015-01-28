from django import forms

from .models import AnnualValue

class AnnualValueForm(forms.ModelForm):
    justification = forms.CharField( widget=forms.Textarea, help_text="Help text for 'justification'- forms.py")
    
    class Meta:
        model = AnnualValue