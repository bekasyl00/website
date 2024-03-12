from django import forms
from .models import document



class docform(forms.ModelForm):
 
    class Meta:
        model=document
        fields=['d_naz','d_doc']