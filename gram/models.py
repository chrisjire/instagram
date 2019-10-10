from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save_profile(self):
        self.save
        
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
    post_image = models.ImageField(upload_to= 'images')
    post_name = models.CharField(max_length=20)
    post_description = models.TextField()
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add= True)
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    @classmethod
    def get_post(cls):
        new = cls.objects.all()
        return new
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'