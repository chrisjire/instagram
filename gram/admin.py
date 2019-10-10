from django.contrib import admin
from .models import Profile, Post, tags

class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post,PostAdmin)
admin.site.register(tags)