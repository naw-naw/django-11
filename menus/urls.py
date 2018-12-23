from django.conf.urls import url

from .views import (
	ItemCreateView,
	ItemListView,
	ItemDetailView,
	ItemUpdateView,
)

urlpatterns = [
    
 	url(r'^create/$',ItemCreateView.as_view(),name='create'),
 	url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(),name='detail'),
 	url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(),name='edit'),
 	url(r'^$', ItemListView.as_view(),name='list'),
]




