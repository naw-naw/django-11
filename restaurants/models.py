from django.db import models
from django.conf import settings
from django.db.models import Q
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.core.urlresolvers import reverse
from .validators import validate_category

User =settings.AUTH_USER_MODEL

class RestaurantLocationQuerySet(models.query.QuerySet):
	# print('1. search in QuerySet====>')
	def search(self,query): #RestaurantLocation.objects.all().search(query) #RestaurantLocation.objects.filter(something).search()
		if query:
			query=query.strip() #/u/naw/?q=%20London (strip space see %20 in search input box)
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
		print('2. queryset in manager====>')
		return RestaurantLocationQuerySet(self.model,using=self._db)

	def search(self,query):   #RestaurantLocation.objects.search()
		print('3. search in manager====>')
		return self.get_queryset().search(query)

class RestaurantLocation(models.Model): #(app)restaurants_(model)restaurantlocation_set
	owner 		=models.ForeignKey(User)
	name 		=models.CharField(max_length=120)
	location 	=models.CharField(max_length=120,null=True,blank=True)
	category	=models.CharField(max_length=120,null=True,blank=True,validators=[validate_category]) #True means can leave blank, False means you must fill this input field
	timestamp	=models.DateTimeField(auto_now_add=True)
	updated		=models.DateTimeField(auto_now=True)
	slug		=models.SlugField(null=True,blank=True)

	objects =RestaurantLocationManager()  #add Model.objects.all()

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('restaurants:detail', kwargs={'slug':self.slug})
		# return reverse('restaurant-detail', kwargs={'slug':self.slug})

	@property
	def title(self):      #use name as title
		return self.name  #==obj.title

def rl_pre_save_receiver(sender,instance,*args,**kwargs):
	print(" ......rl_pre_save_receiver called.......")
	instance.category=instance.category.capitalize()
	if not instance.slug: 	#generate slug as soon as creat new name for new object
		instance.slug=unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver,sender=RestaurantLocation)

# def rl_post_save_receiver(sender,instance,created, *args,**kwargs):
# 	print('saved')
# 	print(instance.timestamp)
# 	if not instance.slug: #generate slug if has already saved name without slug(blank)
# 		instance.slug=unique_slug_generator(instance)
# 		instance.save()

# post_save.connect(rl_post_save_receiver,sender=RestaurantLocation)