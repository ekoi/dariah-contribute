"""
    DARIAH Contribute - DARIAH-EU Contribute: edit your DARIAH contributions.

    Copyright 2014 Data Archiving and Networked Services

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from django.conf.urls import patterns, url
from django.contrib.auth import urls as auth_urls


urlpatterns = auth_urls.urlpatterns  # Password reset and login urls
urlpatterns += patterns('',
    # /lockout displays a message when someone's account is blocked (django-axes)

    #url(r'^/$', 'user_details', ),
    #url(r'^details/$', 'user_details', name="user_details"),
    #url(r'^update/$', 'update_details', name="user_details_update"),
)
