from django.conf.urls import url

from .views import (
	# restaurant_createview,
	# restaurant_listview,
	RestaurantListView,
	RestaurantDetailView,
	RestaurantCreateView,
	RestaurantUpdateView,
)

urlpatterns = [
    
	# url(r'^restaurants/create/$',restaurant_createview),
 	url(r'^create/$',RestaurantCreateView.as_view(),name='create'),
 	url(r'^(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(),name='edit'),  #detail-update,form-snippet.html,
 	url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(),name='detail'),     #template_name='restaurants/detail-update.html'
 	# url(r'^(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(),name='detail'),       #comment out this to work again with above two lines
 	url(r'^$', RestaurantListView.as_view(),name='list'),
 	
 	
]


# url(r'^$', RestaurantListView.as_view(),name='list'),
# # url(r'^restaurants/create/$',restaurant_createview),
# url(r'^create/$',RestaurantCreateView.as_view(),name='create'),
# url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(),name='detail'),
