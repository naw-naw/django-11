from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from restaurants.models import RestaurantLocation

def image_upload_to(instance,filename):  #filename=>iPhone 8,MP3 Player etc..
	title=instance.name
	print("filename in image_upload_to---->",filename)
	slug=slugify(title)
	basename, file_extension=filename.split(".")
	new_filename="%s-%s.%s" %(slug, instance.id, file_extension)
	return "items/%s/%s" %(slug, new_filename)

class Item(models.Model):
	user  		=models.ForeignKey(settings.AUTH_USER_MODEL)
	restaurant	=models.ForeignKey(RestaurantLocation)
	name 		=models.CharField(max_length=120)
	contents 	=models.TextField(help_text="separate each item by coma")
	excludes 	=models.TextField(blank=True,null=True,help_text='separate each item by comma')
	public 		=models.BooleanField(default=True)
	timestamp	=models.DateTimeField(auto_now_add=True)
	updated		=models.DateTimeField(auto_now=True)
	image 		=models.ImageField(upload_to=image_upload_to,blank=True)

	def get_absolute_url(self):
		return reverse('menus:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.name
		
	class Meta:
		ordering=['-updated','-timestamp'] #get most recently updated item first

	def get_contents(self):
		return self.contents.split(",")

	def get_excludes(self):
		return self.excludes.split(",")