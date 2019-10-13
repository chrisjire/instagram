from django.shortcuts import render, redirect, get_object_or_404
import datetime as dt
from .models import Post, Profile, NewsletterRecipients, User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .email import send_welcome_email
from .forms import NewsLetterForm, ProfileForm, PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    images = Post.objects.all()
    
    if request.method == 'POST':
        form = NewsLetterForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsletterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)
            
            HttpResponseRedirect('welcome')
    else:
        form = NewsLetterForm()
    
    return render (request, 'index.html', {"images":images, "letterForm":form},locals())

@login_required(login_url='/accounts/login/')
def profile(request):
    images = request.user.profile.posts.all()
    user_object = request.user
    user_images = user_object.profile.posts.all()
    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method == 'POST':
        print(request.FILES)
        new_profile = ProfileForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        
        if new_profile.is_valid():
            new_profile.save()
            print(new_profile.fields)
            return redirect('profile')
    else:
        new_profile = ProfileForm(instance=request.user.profile)
    return render(request, 'edit.html', locals())

@login_required(login_url='/accounts/login/')
def new_post(request):
    image_form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            request.user.profile.posts(form)
    return render(request, 'new_post.html', locals())

@login_required(login_url='/accounts/login/')
def user(request, user_id):
    user_object=get_object_or_404(User, pk=user_id)
    if request.user == user_object:
        return redirect('profile')
    # isfollowing = user_object.profile not in request.user.profile.follows
    user_images = user_object.profile.posts.all()
    return render(request, 'userprofile.html', locals())

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_user(search_term)
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"profiles":searched_profiles})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})


