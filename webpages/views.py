from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from gc import get_objects
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.templatetags.static import static
# from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    
    
    return render(request, 'index.html')



def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']  
        
        user = authenticate (request,username=username,password=password)
        if user is not None:
            login(request,user)
            alert("you're logged in!")
            messages.success(request,"Welcome , you are now logged in")
            return redirect ("index")
    return render(request, 'index.html')




def register(request):
    
    if request.method =='POST':
       
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 != password2:
            messages.error(request,"confirm your passwords")
            return redirect('index')

        
        new_user = User.objects.create_user(username=username,email=email,password=password1)
       
        
        new_user.save()
        return render(request,'index.html')
    return render(request, 'index.html')

def signout(request):
    logout(request)
    messages.success(request,"You have logged out")
           
    return redirect("/")

