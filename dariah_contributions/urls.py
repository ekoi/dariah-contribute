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
    url(r'^all/$', ListView.as_view(model=Contribution, queryset=Contribution.published.all()), name='list'),
    # example: /dariah_contributions/detail/5/
    url(r'^add/$', ContributionCreate.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/update/$', ContributionUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', ContributionDelete.as_view(), name='delete'),
    url(r'^(?P<pk>\d+)\.xml$', ContributionRDF.as_view(), name='detail_rdf'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Contribution, queryset=Contribution.published.all()), name='detail'),
    # example: /dariah_contributions/detail_rdf/5/

)
