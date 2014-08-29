from django.contrib import admin
from dariah_static_data.models import TADIRAHTechnique, TADIRAHActivity, TADIRAHObject, TADIRAHVCC, Country, Discipline

admin.site.register(TADIRAHTechnique)
admin.site.register(TADIRAHActivity)
admin.site.register(TADIRAHObject)
admin.site.register(TADIRAHVCC)
admin.site.register(Country)
admin.site.register(Discipline)
