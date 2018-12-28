# from django.contrib.auth import authenticate,login,get_user_model
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect

from django.core.mail import send_mail
from django.views.generic import ListView
from menus.models import Item
from .forms import ContactForm 			#LoginForm,RegisterForm

def home_page(request):
	items=Item.objects.all()
	context={
		"items":items
	}
	if request.user.is_authenticated():
		context["premium_content"]="Premium Service"
	return render(request,"home_page.html",context)

def about_page(request):
	context={
		"title":"About Page",
		"content": "Welcome to the about page",
	}
	return render(request,"about_page.html", context)

def contact_page(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_full_name = form.cleaned_data.get("full_name")
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'naw@gmail.com']
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "contact_page.html", context)



