from django.db import models
from django.conf import settings
from django.db.models import Q
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.core.urlresolvers import reverse
from .validators import validate_category

User =settings.AUTH_USER_MODEL

class RestaurantLocationQuerySet(models.query.QuerySet):
	def search(self,query):
		if query:
			query=query.strip() 
			return self.filter(
				Q(name__icontains=query)|
				Q(location__icontains=query)|
				Q(location__iexact=query)|
				Q(category__icontains=query)|
				Q(category__iexact=query)|
				Q(item__name__icontains=query)|
				Q(item__contents__icontains=query)
				).distinct()
		return self

class RestaurantLocationManager(models.Manager):
	def get_queryset(self):
		return RestaurantLocationQuerySet(self.model,using=self._db)

	def search(self,query):   #RestaurantLocation.objects.search()
		
		return self.get_queryset().search(query)

class RestaurantLocation(models.Model):
	owner 		=models.ForeignKey(User)
	name 		=models.CharField(max_length=120)
	location 	=models.CharField(max_length=120,null=True,blank=True)
	category	=models.CharField(max_length=120,null=True,blank=True,validators=[validate_category])
	timestamp	=models.DateTimeField(auto_now_add=True)
	updated		=models.DateTimeField(auto_now=True)
	slug		=models.SlugField(null=True,blank=True)

	objects =RestaurantLocationManager()  

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('restaurants:detail', kwargs={'slug':self.slug})
		

	@property
	def title(self):      
		return self.name 

def rl_pre_save_receiver(sender,instance,*args,**kwargs):
	print(" ......rl_pre_save_receiver called.......")
	instance.category=instance.category.capitalize()
	if not instance.slug: 	
		instance.slug=unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver,sender=RestaurantLocation)

# def rl_post_save_receiver(sender,instance,created, *args,**kwargs):
# 	print('saved')
# 	print(instance.timestamp)
# 	if not instance.slug:
# 		instance.slug=unique_slug_generator(instance)
# 		instance.save()

# post_save.connect(rl_post_save_receiver,sender=RestaurantLocation)
