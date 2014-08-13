from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import urls as auth_urls


admin.autodiscover()
urlpatterns = auth_urls.urlpatterns  # Password reset and login urls

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dariah_contributions/', include('dariah_contributions.urls', namespace="dariah_contributions")),
    # Login/Logout URL
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    # /accounts/lockout displays a message when someone's account is blocked (django-axes)
)

#urlpatterns += patterns(settings.APPS_PREFIX + 'contact_data.views',
#    (r'^accounts/$', 'user_details', ),
#    url(r'^accounts/details/$', 'user_details', name="user_details"),
#    url(r'^accounts/update/$', 'update_details', name="user_details_update"),
#    url(r'^accounts/change-password/$', 'change_password', name="change_password"),
#)
