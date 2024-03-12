from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import userform,profilimage,userupdeteform
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method=="POST":
        form=userform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Пользователь {username} был успешно создан!')
            return redirect('home')
    else:
        form=userform()
    
    
    
    return render(request,'users/register.html',{'title':'registration','form':form})
@login_required
def profil(request):
    if request.method=="POST":
        profilform=profilimage(request.POST,request.FILES,instance=request.user.profil)
        updateuserform=userupdeteform(request.POST ,instance=request.user)
        if profilform.is_valid() and updateuserform.is_valid():
            updateuserform.save()
            profilform.save()
            messages.success(request,f'Ваш аккаунт успешно обнавлено!')
            return redirect('profil')
    else:
        profilform=profilimage(instance=request.user.profil)
        updateuserform=userupdeteform(instance=request.user)
    data={'profilform':profilform,'updateuser':updateuserform}
    return render(request,'users/profil.html',data)
    