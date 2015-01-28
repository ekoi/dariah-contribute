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
from django.contrib import admin


from dariah_annual_value.views import AnnualValueCreate, AnnualValueDetail

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'dariah_annual_value.views.join', name='join'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^detail/$', AnnualValueDetailMixin.as_view(), name='detail'),
   
    #url(r'^$', 'dariah_annual_value.views.join', name='join'),
    url(r'^$', AnnualValueCreate.as_view(), name='add'),
    #url(r'^(?P<pk>\d+)/detail/$', AnnualValueDetailMixin.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)\.html$', AnnualValueDetail.as_view(), name='detail_html'),
    url(r'^(?P<pk>\d+)/$', AnnualValueDetail.as_view(), name='detail'),
)
