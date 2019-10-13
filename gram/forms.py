from django import forms
from .models import Profile

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']