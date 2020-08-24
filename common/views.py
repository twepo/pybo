from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django import forms
from django.contrib.auth.forms import UserCreationForm





# 로그인기능이 있나

from common.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username,password=raw_password)

            login(request,user)
    # 내가봤을때.. request를 넣어주는건 csrf 이다! 
            return redirect("index")
    else:
        form = UserForm()
    return render(request,'common/signup.html',{"form":form} )
        

def page_not_found(request,exception):
    print(exception)
    return render(request,'common/404.html',{})