from django.shortcuts import render, redirect
import datetime as dt
from .models import Post, Profile
from django.http import HttpResponse
from .email import send_welcome_email
from .forms import NewsLetterForm

# Create your views here.
def welcome(request):
    new = Post.get_post()
    prof = Profile.get_profile()
    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = NewsLetterForm()
    
    return render (request, 'index.html', {"new":new, "prof":prof, "letterForm":form})


