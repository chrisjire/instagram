from django.shortcuts import render, redirect
import datetime as dt
from .models import Post, Profile

# Create your views here.
def welcome(request):
    new = Post.get_post()
    prof = Profile.get_profile()
    return render (request, 'index.html', {"new":new}, {"prof":prof})

