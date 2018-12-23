from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from .models import RestaurantLocation
from .forms import RestaurantLocationCreateForm#,RestaurantCreateForm,

# def restaurant_listview(request):
# 	template_name='restaurants/restaurantlocation_list.html'
# 	queryset=RestaurantLocation.objects.all()
# 	context={
# 		"object":queryset
# 	}
# 	return render(request,template_name,context)

class RestaurantListView(LoginRequiredMixin,ListView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)  #only my restaurants(naw), or james if you loged in james
	# def get_queryset(self):
	# 	slug=self.kwargs.get("slug")
	# 	if slug:
	# 		queryset=RestaurantLocation.objects.filter(
	# 			Q(category__iexact=slug)|  			#iexact means exact name e.g mexican
	# 			Q(category__icontains=slug)			#icontains any name if there is slug
	# 			)
	# 	else:
	# 		queryset=RestaurantLocation.objects.all()
	# 	return queryset

class RestaurantDetailView(LoginRequiredMixin,DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class=RestaurantLocationCreateForm  #modelForm class
	template_name='form.html'      	#restaurants/
	login_url='/login/'   			#this override LOGIN_URL in settings.py
	# success_url='/restaurants/'

	def form_valid(self,form):
		instance=form.save(commit=False)
		instance.owner=self.request.user
		# instance.save() # no need this if used below line
		return super(RestaurantCreateView,self).form_valid(form) # this calls form.save()

	def get_context_data(self,*args,**kwargs):
		context=super(RestaurantCreateView,self).get_context_data(*args,**kwargs)
		context['title']='Add Restaurant'
		return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class=RestaurantLocationCreateForm  #modelForm class
	template_name='form.html'      	#restaurants/
	# template_name='restaurants/detail-update.html'
	login_url='/login/'   			#this override LOGIN_URL in settings.py
	# success_url='/restaurants/'

	def get_context_data(self,*args,**kwargs):
		context=super(RestaurantUpdateView,self).get_context_data(*args,**kwargs)
		name=self.get_object().name
		context['title']=f'Update Restaurant: {name}'
		return context

	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user) 




# @login_required()		#login_url='/login/')
# def restaurant_createview(request):
# 	form=RestaurantLocationCreateForm(request.POST or None)  # direct go to context{} to provide blank form
# 	errors=None
# 	if form.is_valid():
# 		if request.user.is_authenticated:
# 			instance=form.save(commit=False)
# 			instance.owner=request.user
# 			instance.save()  
# 			return HttpResponseRedirect('/restaurants/')
# 		else:
# 			return HttpResponseRedirect('/login/')		
# 	if form.errors:
# 		errors=form.errors
# 	template_name='restaurants/form.html'	
# 	context={
# 		'form':form,
# 		'errors':errors
# 	}
# 	return render(request,template_name,context)


# class RestaurantDetailView(DetailView):
# 	queryset=RestaurantLocation.objects.all()
	# template_name='restaurants/restaurantlocation_detail.html'

	# def get_object(self,*args,**kwargs):
	#  	rest_id=self.kwargs.get('slug')
	#  	obj=get_object_or_404(RestaurantLocation,slug=slug)
	#  	return obj

	# def get_context_data(self,*args,**kwargs):
	# 	print(self.kwargs)
	# 	context=super(RestaurantDetailView,self).get_context_data(*args,**kwargs)
	# 	print(context)
	# 	return context

# class SearchRestaurantListView(ListView):
# 	# queryset=RestaurantLocation.objects.filter(category__iexact='mexican')
# 	template_name='restaurants/restaurants_list.html'

# 	def get_queryset(self):
# 		slug=self.kwargs.get('slug')
# 		if slug:
# 			queryset=RestaurantLocation.objects.filter(
# 				Q(category__iexact=slug)|  			#iexact means exact name e.g mexican
# 				Q(category__icontains=slug)			#icontains any name if there is slug
# 				)
# 		else:
# 			queryset=RestaurantLocation.objects.none()
# 		return queryset
	
# class AsianFusionRestaurantListView(ListView):
# 	queryset=RestaurantLocation.objects.filter(category__iexact='asian fusion')
# 	template_name='restaurants/restaurants_list.html'


# class HomeView(TemplateView):
# 	template_name='home.html'
# 	def get_context_data(self,*args,**kwargs):
# 		context=super(HomeView,self).get_context_data(*args,**kwargs)
# 		return context

# class AboutView(TemplateView):
# 	template_name='about.html'

# class ContactView(TemplateView):
# 	template_name='contact.html'

# class ContactView(View):
# 	def get(self,request,*args,**kwargs):
# 		print("kwargs===>",kwargs)
# 		context={
# 		}
# 		return render(request,"contact.html", context)
