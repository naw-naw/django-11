from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import DetailView,View
# Create your views here.
from menus.models import Item
from restaurants.models import RestaurantLocation
from .models import Profile 

User=get_user_model()

class ProfileFollowToggle(LoginRequiredMixin,View):
	def post(self,request,*args,**kwargs):
		user_to_toggle=request.POST.get('username')
		profile_=Profile.objects.get(user__username__iexact=user_to_toggle)
		user =request.user
		if user in profile_.followers.all():
			profile_.followers.remove(user)
		else:
			profile_.followers.add(user)
		return redirect(f"/u/{profile_.user.username}/")

class ProfileDetailView(DetailView):
	# queryset=User.objects.filter(is_active=True)
	template_name='profiles/user.html'

	def get_object(self):  
		username=self.kwargs.get('username')
		if username is None:
			raise Http404
		return get_object_or_404(User,username__iexact=username,is_active=True)

	def get_context_data(self,*args,**kwargs):
		 context=super(ProfileDetailView,self).get_context_data(*args,**kwargs)
		 user=context['user']
		 query=self.request.GET.get('q')
		 items_exists=Item.objects.filter(user=user).exists()
		 qs=RestaurantLocation.objects.filter(owner=user).search(query)
		 # if query:
		 # 	qs=qs.search(query)
		 	# qs=RestaurantLocation.objects.search(query)
		 if items_exists and qs.exists():
		 	context['locations']=qs
		 return context

