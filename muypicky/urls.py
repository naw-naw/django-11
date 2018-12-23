from django.conf.urls import url,include
from django.contrib import admin
#from restaurants.views import HomeView #AboutView,ContactView #home,contact,about,
from django.views.generic import TemplateView

from django.contrib.auth.views import LoginView
from profiles.views import ProfileFollowToggle

# from restaurants.views import (
# 	restaurant_createview,
# 	restaurant_listview,
# 	RestaurantListView,
# 	RestaurantDetailView,
# 	RestaurantCreateView,
# )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',TemplateView.as_view(template_name='home.html'),name='home'),
    url(r'^login/$', LoginView.as_view(),name='login'),
    url(r'^profile-follow/$',ProfileFollowToggle.as_view(),name='follow'),
    url(r'^u/', include('profiles.urls',namespace='profiles')), #menus=appname
    url(r'^items/', include('menus.urls',namespace='menus')), 
    url(r'^restaurants/', include('restaurants.urls',namespace='restaurants')), #restaurants=appname
 	url(r'^about/$',TemplateView.as_view(template_name='about.html'),name='about'),
 	url(r'^contact/$',TemplateView.as_view(template_name='contact.html'),name='contact'), 	

]




# url(r'^restaurants/$', RestaurantListView.as_view(),name='restaurants'),
#  	# url(r'^restaurants/create/$',restaurant_createview),
#  	url(r'^restaurants/create/$',RestaurantCreateView.as_view(),name='restaurants-create'),
#  	url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(),name='restaurant-detail'),