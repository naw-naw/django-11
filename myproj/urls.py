from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include
from django.contrib import admin
#from restaurants.views import HomeView #AboutView,ContactView #home,contact,about,
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from profiles.views import ProfileFollowToggle
from .views import home_page,contact_page,about_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page,name='home'),
	url(r'^about/$', about_page,name='about'),
	url(r'^contact/$', contact_page,name='contact'),
    url(r'^$',TemplateView.as_view(template_name='home.html'),name='home'),
    url(r'^login/$', LoginView.as_view(),name='login'),
    url(r'^profile-follow/$',ProfileFollowToggle.as_view(),name='follow'),
    url(r'^u/', include('profiles.urls',namespace='profiles')), #menus=appname
    url(r'^items/', include('menus.urls',namespace='menus')), 
    url(r'^restaurants/', include('restaurants.urls',namespace='restaurants')), #restaurants=appname
#  	url(r'^about/$',TemplateView.as_view(template_name='about_page.html'),name='about'),
#  	url(r'^contact/$',TemplateView.as_view(template_name='contact_page.html'),name='contact'), 	
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

