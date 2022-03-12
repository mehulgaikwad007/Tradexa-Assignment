from django.contrib.auth import authenticate
from django.shortcuts import render , redirect
from .forms import LoginForm, RegisterForm 
from django.http import HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib import messages

from .models import Post, User

# Create your views here.

def home(request):
    return render(request,'home.html')

def register_view(request):
    r_form = RegisterForm(request.POST or None)
    if r_form.is_valid():
        user = r_form.save(commit=False)
        password = r_form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(email = user.email , password=password)
        auth.login(request,new_user)
        return redirect("User:login_view")
    

    return render(request,'register.html',{'r_form':r_form})
    
def login_view(request):

    
    l_form = LoginForm(request.POST or None)
    if l_form.is_valid():
        email = l_form.cleaned_data.get('email')
        password = l_form.cleaned_data.get('password')

        user = authenticate(email=email, password = password)
        auth.login(request,user)
        return redirect("User:post")
        
        

    return render(request,'login.html',{'l_form':l_form})

def logout_view(request):
    auth.logout(request)
    return render(request,'home.html')

def viewpost(request):
    
    user = request.user
    post_all = Post.objects.filter(user=user)
    return render(request,'post.html',{'post_all':post_all})


def createpost(request):
    user = request.user
    
    
    if request.method == "POST":
        text = request.POST.get('text', '')
        Post(text=text,user=user).save()

        return redirect("User:post")

    return render(request,'createpost.html')
    
    
def updatePost(request,id):
    
    post = Post.objects.filter(id=id)
    p=Post.objects.get(id=id)
    if request.method=="POST":
        text = request.POST.get('text')
        p.text=text
        p.save()
        #post.update(text=text)
        
        return redirect('/post')
    return render(request,'updatepost.html',{'post':post})

    
