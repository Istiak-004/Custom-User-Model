from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *


def Home(request):
    return render(request,'usertemp/home.html')

def RegisterFormView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:        
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request,'usertemp/register.html',context)

# def LoginView(request):
#     if request.method == 'POST':
#         form  = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             # user = form.get_user()
#             # login(request,user)
#             # return redirect('home')
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             user = authenticate(request,username = email,password = password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('home')
#             else:
#                 return redirect('register')
#     else:
#         form = AuthenticationForm()
#     context = {
#         'form':form
#     }  
#     return render(request,'usertemp/login.html',context)

def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request,email = email,password = password)
            if user is not None:
                login(request,user)
                return redirect('home')
        else:
            print('Error')
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request,'usertemp/login.html',context)





