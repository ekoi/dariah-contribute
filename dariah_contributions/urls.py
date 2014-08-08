from django.conf.urls import patterns, url

from dariah_contributions import views

urlpatterns = patterns('',
    # example: /dariah_contributions/
     url(r'^$', views.index, name='index'),
    # example: /dariah_contributions/list/
    url(r'^list/$', views.list_view.as_view(), name='list'),
    # example: /dariah_contributions/detail/5/
    url(r'^detail/(?P<pk>\d+)/$', views.detail_view.as_view(), name='detail'),
    # example: /dariah_contributions/detail_rdf/5/
    url(r'^detail_rdf/(?P<pk>\d+)/$', views.detail_view_rdf, name='detail_rdf'),
    # example: /dariah_contributions/contribution/5/
    url(r'^contribution/(?P<contribution_id>\d+)/$', views.contribution, name='contribution'),
    # example: /dariah_contributions/logout/
    url(r'^logout/$', views.dariah_logout, name='logout'),
)


