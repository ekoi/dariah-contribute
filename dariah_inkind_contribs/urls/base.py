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

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),

    url(r'^$', RedirectView.as_view(url='/about/', permanent=False)),
    url(r'^contribution/', include('dariah_inkind.urls', namespace="dariah_inkind")),
    url(r'^accounts/', include('dariah_accounts.urls')),  # NOTE: this one should NOT have a namespace
    #url(r'^signup/', include('signups.urls')), 
    url(r'^annual-value/', include('dariah_annual_value.urls', namespace="dariah_annual_value")), 
)
