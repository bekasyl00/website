
from django import forms
from .models import Profil
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
class userform(UserCreationForm):
    email=forms.EmailField(label='Введие Email',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    username=forms.CharField(label='Введите имя',required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Введите пароль',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
                           
    password2=None
    class Meta:
        model=User
        fields=['email','username','password1']
class userupdeteform(forms.ModelForm):
        
    username=forms.CharField(label='Введите имя',required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label='Введие Email',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email']
class profilimage(forms.ModelForm):
    img=forms.ImageField(label='Выберайте фотографий',required=False,widget=forms.FileInput(attrs={'class':'imgb'}))
    class Meta:
       
        model=Profil
        fields=['img']

            
            
            