from django import forms
from .models import *

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    
class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget=forms.TextInput()
    class Meta:
        model = Profile
        fields = ('profile_image','first_name','last_name','bio' )
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'pub_date')
        
        