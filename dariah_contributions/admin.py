from django.contrib import admin
from dariah_contributions.models import Contribution


class ContributionAdmin(admin.ModelAdmin):
    fields = ['dc_title', 'published_on']
    list_filter = ['published_on', ]

admin.site.register(Contribution, ContributionAdmin)
