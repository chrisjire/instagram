from django.shortcuts import render, redirect
import datetime as dt
from .models import Post, Profile
from django.http import HttpResponse
from .email import send_welcome_email

# Create your views here.
def welcome(request):
    new = Post.get_post()
    prof = Profile.get_profile()
    return render (request, 'index.html', {"new":new}, {"prof":prof})


