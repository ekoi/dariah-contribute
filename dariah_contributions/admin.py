from django.contrib import admin
from dariah_contributions.models import Contribution

class ContributionAdmin(admin.ModelAdmin):
    fields = ['title', 'contributor', 'publish_date']
    list_filter = ['contributor', 'publish_date']
        
admin.site.register(Contribution, ContributionAdmin)
