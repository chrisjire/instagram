from django.shortcuts import render, redirect
import datetime as dt
from .models import Post, Profile, NewsletterRecipients
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .email import send_welcome_email
from .forms import NewsLetterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    new = Post.get_post()
    prof = Profile.get_profile()
    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsletterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)
            
            HttpResponseRedirect('welcome')
    else:
        form = NewsLetterForm()
    
    return render (request, 'index.html', {"new":new, "prof":prof, "letterForm":form})


