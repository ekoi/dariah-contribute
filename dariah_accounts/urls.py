from django.conf.urls import patterns, url
from django.contrib.auth import urls as auth_urls


urlpatterns = auth_urls.urlpatterns  # Password reset and login urls
urlpatterns += patterns('',
    # /lockout displays a message when someone's account is blocked (django-axes)

    #url(r'^/$', 'user_details', ),
    #url(r'^details/$', 'user_details', name="user_details"),
    #url(r'^update/$', 'update_details', name="user_details_update"),
)
