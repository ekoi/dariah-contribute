from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),

    url(r'^$', RedirectView.as_view(url='/about/', permanent=False)),
    url(r'^contribution/', include('dariah_core.urls', namespace="dariah_core")),
    url(r'^accounts/', include('dariah_accounts.urls')),  # NOTE: this one should NOT have a namespace
)
