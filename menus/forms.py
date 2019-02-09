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
			'public',
			'image',
		]
		
	#when http://127.0.0.1:8000/items/create/
	def __init__(self,user=None,*args,**kwargs):
		
		super(ItemForm,self).__init__(*args,**kwargs) #call super form
		self.fields['restaurant'].queryset=RestaurantLocation.objects.filter(owner=user) #filter items owned by user, not owned by other user
		

