from django.contrib import admin

# Register your models here.

from .models import AnnualValue

from django import forms


        
        
class AnnualValueForm(forms.ModelForm):
    justification = forms.CharField( widget=forms.Textarea, help_text="Help text for 'justification'-annualvalue form")
    class Meta:
        model = AnnualValue

class AnnualValueAdmin(admin.ModelAdmin):
    justification = forms.CharField( widget=forms.Textarea, help_text="Help text for 'justification'-annualvalue form2")
    form = AnnualValueForm
    list_display = ['id', 'inkind', 'materialcost', 'personnelcost', 'year', 'justification']
    
admin.site.register(AnnualValue, AnnualValueAdmin)