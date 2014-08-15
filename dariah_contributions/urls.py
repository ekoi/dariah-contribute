from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Contribution
from .views import ContributionCreate, ContributionDelete, ContributionUpdate, ContributionRDF, MyContributions


urlpatterns = patterns('',
    url(r'^(all/)?$', ListView.as_view(model=Contribution, queryset=Contribution.published.all()), name='list'),
    # example: /contribution/
    # example: /contribution/all/
    url(r'^mine/$', MyContributions.as_view(), name='mine'),
    url(r'^add/$', ContributionCreate.as_view(), name='add'),
    # example: /contribution/add/
    url(r'^(?P<pk>\d+)/update/$', ContributionUpdate.as_view(), name='update'),
    # example: /contribution/5/update/
    url(r'^(?P<pk>\d+)/delete/$', ContributionDelete.as_view(), name='delete'),
    # example: /contribution/5/delete/
    url(r'^(?P<pk>\d+)\.xml$', ContributionRDF.as_view(), name='detail_rdf'),
    # example: /contribution/detail_rdf/5/
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Contribution, queryset=Contribution.published.all()), name='detail'),
    # example: /contribution/5/
)
