from django.contrib.auth.mixins import LoginRequiredMixin  
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Item
from .forms import ItemForm
# Create your views here.

class ItemListView(ListView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemDetailView(DetailView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemCreateView(LoginRequiredMixin,CreateView):
	template_name='form.html'  #from main templates
	form_class=ItemForm

	def form_valid(self,form):
		obj=form.save(commit=False)
		obj.user=self.request.user  #no need obj.save()
		return super(ItemCreateView,self).form_valid(form) #this line does save ->obj.user

	def get_form_kwargs(self):  #call ItemForm.__init__(forms.py) and passed 'user'
		#print('get_form-called')
		kwargs=super(ItemCreateView,self).get_form_kwargs()
		# print('kwargs=====>',kwargs)  #  {'initial': {}, 'prefix': None, 'instance': None}
		kwargs['user']=self.request.user
		# kwargs['instance']=Item.objects.filter(user=self.request.user).first()
		return kwargs

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self,*args,**kwargs):
		context=super(ItemCreateView,self).get_context_data(*args,**kwargs)
		context['title']='Create Item'
		return context

class ItemUpdateView(LoginRequiredMixin,UpdateView):
	template_name='form.html'
	form_class=ItemForm

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)
	
	def get_context_data(self,*args,**kwargs):
		context=super(ItemUpdateView,self).get_context_data(*args,**kwargs)
		# print('context in ItemUpdate===>',context)
		context['title']='Update Item'
		return context

	def get_form_kwargs(self): #this call ItemForm(forms.py) and get item name(3 or 2),with restaurant name to update
		kwargs=super(ItemUpdateView,self).get_form_kwargs()
		kwargs['user']=self.request.user
		print('kwargs====>',kwargs)
		return kwargs



