from django.contrib.auth import get_user_model

User=get_user_model()

random_ =User.objects.last()

#my followers 
random_.profile.followers.all()

#followers	=models.ManyToManyField(User,related_name='is_following',blank=True)
#who i follow  
random_.is_following.all() #==random_.profile.following.all()

# following	=models.ManyToManyField(User,related_name='following',blank=True)