from django.contrib import admin

# Register your models here.

from .models import AnnualValue

from django import forms


        
        
class AnnualValueForm(forms.ModelForm):
    justification = forms.CharField( widget=forms.Textarea, help_text="Write down the justification of the project.")
    class Meta:
        model = AnnualValue

class AnnualValueAdmin(admin.ModelAdmin):
    form = AnnualValueForm
    list_display = ['id', 'inkind', 'value', 'year', 'justification']
admin.site.register(AnnualValue, AnnualValueAdmin)
#admin.site.register(AnnualValue, AnnualValueAdmin)