from django import forms
from django.forms import ModelForm
from dariah_contributions import models

class ContributionForm(ModelForm):
    class Meta:
        model = models.Contribution
        fields = ['title', 'date', 'relation', 'publisher', 'coverage', 'subject', 'abstract', 'description', 'contributor', 'vocabulary', ]
        widgets = {
            'abstract': forms.Textarea(attrs={'cols': 80, 'rows': 10}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'date': forms.DateTimeInput(attrs={"size":10}),
        }
    
