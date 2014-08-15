from django.contrib import admin
from dariah_contributions.models import Contribution, DcCreator, DcContributor


class ContributionAdmin(admin.ModelAdmin):
    list_filter = ['published_on', ]
    readonly_fields = ['author', 'last_modified_on', 'dc_identifier']
    filter_horizontal = ['dc_creator', 'dc_contributor']

admin.site.register(DcCreator)
admin.site.register(DcContributor)
admin.site.register(Contribution, ContributionAdmin)
