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

from .views import ContributionCreate
from .views import ContributionDelete
from .views import ContributionUpdate
from .views import ContributionPublish
from .views import ContributionUnpublish
from .views import MyContributions
from .views import ContributionDetail
from .views import ContributionHybridDetail
from .views import ContributionRDF
from .views import ContributionList
from .views import DcCreatorCreate
from .views import DcContributorCreate
from .views import ContributionsFeed
from .views import ContributionsAtomFeed


urlpatterns = patterns('',
    url(r'^(all/)?$', ContributionList.as_view(), name='list'),
    # example: /contribution/
    # example: /contribution/all/
    url(r'^mine/$', MyContributions.as_view(), name='mine'),
    url(r'^add/$', ContributionCreate.as_view(), name='add'),
    # example: /contribution/add/
    url(r'^(?P<pk>\d+)/update/$', ContributionUpdate.as_view(), name='update'),
    # example: /contribution/5/update/
    url(r'^(?P<pk>\d+)/delete/$', ContributionDelete.as_view(), name='delete'),
    # example: /contribution/5/delete/
    url(r'^(?P<pk>\d+)/publish/$', ContributionPublish.as_view(), name='publish'),
    # example: /contribution/5/publish/
    url(r'^(?P<pk>\d+)/unpublish/$', ContributionUnpublish.as_view(), name='unpublish'),
    # example: /contribution/5/unpublish/
    url(r'^(?P<pk>\d+)\.xml$', ContributionRDF.as_view(), name='detail_rdf'),
    # example: /contribution/5.xml
    url(r'^(?P<pk>\d+)\.html$', ContributionDetail.as_view(), name='detail_html'),
    # example: /contribution/5.html
    url(r'^(?P<pk>\d+)/$', ContributionHybridDetail.as_view(), name='detail'),
    # example: /contribution/5/
    # example: /contribution/5?format=html
    # example: /contribution/5/?format=html
    # example: /contribution/5?format=xml
    # example: /contribution/5/?format=xml
    url(r'^dc_creator/add/$', DcCreatorCreate.as_view(), name='dccreator_create'),
    url(r'^dc_contributor/add/$', DcContributorCreate.as_view(), name='dccontributor_create'),

    url(r'^feed/$', ContributionsFeed(), name='feed'),
    url(r'^feed/rss/$', ContributionsFeed(), name='feed_rss'),
    url(r'^feed/atom/$', ContributionsAtomFeed(), name='feed_atom'),
)
