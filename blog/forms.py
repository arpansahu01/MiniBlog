from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import Post

class usersignupform(UserCreationForm):
    password1 =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
class userloginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'})) 
    password =forms.CharField(widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))    


class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['title','desc']
        labels = {'title':'Title','desc':'Description'}
        widgets = {'title':forms.TextInput(attrs= {'class':'form-control'}),
        'desc':forms.Textarea(attrs={'class':'form-control'})
        }

