from django.conf.urls import patterns, url
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import RedirectView

from .models import Contribution
from .views import ContributionCreate, ContributionDelete, ContributionUpdate, ContributionRDF


urlpatterns = patterns('',
    # example: /dariah_contributions/
    url(r'^$', RedirectView.as_view(url='list'), name='index'),
    # example: /dariah_contributions/list/
    url(r'^list/$', ListView.as_view(model=Contribution, queryset=Contribution.published.all()), name='list'),
    # example: /dariah_contributions/detail/5/
    url(r'^contribution/add/$', ContributionCreate.as_view(), name='add'),
    url(r'^contribution/(?P<pk>\d+)/update/$', ContributionUpdate.as_view(), name='update'),
    url(r'^contribution/(?P<pk>\d+)/delete/$', ContributionDelete.as_view(), name='delete'),
    url(r'^contribution/(?P<pk>\d+)\.xml$', ContributionRDF.as_view(), name='detail_rdf'),
    url(r'^contribution/(?P<pk>\d+)/$', DetailView.as_view(model=Contribution, queryset=Contribution.published.all()), name='detail'),
    # example: /dariah_contributions/detail_rdf/5/

)
