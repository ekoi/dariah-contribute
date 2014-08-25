from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.views.generic.base import RedirectView


admin.autodiscover()
urlpatterns = auth_urls.urlpatterns  # Password reset and login urls

urlpatterns += patterns('',
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    # /lockout displays a message when someone's account is blocked (django-axes)

    url(r'^$', RedirectView.as_view(url='/about/', permanent=False)),
    url(r'^contribution/', include('dariah_contributions.urls', namespace="dariah_contributions")),
)
