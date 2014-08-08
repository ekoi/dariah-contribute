from django import forms
from django.forms import ModelForm
from dariah_contributions import models

class ContributionForm(ModelForm):
    class Meta:
        model = models.Contribution
        fields = ['title', 'contributor', 'description', 'publish_date']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'publish_date': forms.DateTimeInput(attrs={'readonly':'readonly', "size":21}),
        }
    
