from django import forms
from restaurants.models import RestaurantLocation
from .models import Item

class ItemForm(forms.ModelForm):
	class Meta:
		model=Item
		fields=[
			'restaurant',
			'name',
			'contents',
			'excludes',
			'public'
		]
		
	#when http://127.0.0.1:8000/items/create/
	def __init__(self,user=None,*args,**kwargs):
		print('__init__ called===>')
		# print(kwargs.pop('user'))
		# print('user in ItemForm===>',user)
		#print('kwargs===>',kwargs)
		# print('instance==>',kwargs.pop('instance'))
		super(ItemForm,self).__init__(*args,**kwargs) #call super form
		self.fields['restaurant'].queryset=RestaurantLocation.objects.filter(owner=user) #filter items owned by user, not owned by other user
		#self.fields['restaurant'].queryset=RestaurantLocation.objects.none() #clear all data in Restaurant's check box list in ItemForm


#self.fields['restaurant'].queryset=RestaurantLocation.objects.filter(owner=user) #filter items owned by user, not owned by other user //.exclude(item__isnull=False)
#when items/3/update, get item Name associated with 3,let you update 


#self.fields['restaurant'].queryset=RestaurantLocation.objects.filter(owner=user).exclude(item__isnull=False)
# this clear an item asscociated with restaurant name  when set exclude is_null 
