from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.urls import reverse 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    bio = models.TextField(default="Hello Friends")
    
    def __str__(self):
        return f'{self.user.username}'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def search_by_user(cls,search_term):
        profiles = cls.objects.filter(user__name__icontains=search_term)
        return profiles
    
    def post(self, form):
        image = form.save(commit=False)
        image.user = self
        image.save()
        
        
    class Meta:
        ordering = ['user']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class tags(models.Model):
    name = models.CharField(max_length= 20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        
class Post(models.Model):
    image = models.ImageField(upload_to= 'images/')
    post_name = models.CharField(max_length=20)
    post_caption = models.TextField()
    user = models.ForeignKey(User, related_name='posts')
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add= True)
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    @classmethod
    def get_post(cls):
        images = cls.objects.all()
        return images
    
    class Meta:
        ordering = ["-pk"]
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
    def get_absolute_url(self):
        return reverse('welcome')
class NewsletterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    