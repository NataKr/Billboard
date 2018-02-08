# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Post
from .forms import UserLoginForm, UserRegisterForm
import datetime
from django.contrib.auth import (authenticate,
                                 get_user_model,
                                login, logout,
                                 )
# Create your views here.

def index(request):
    pass

    #post_list = Post.objects.all()
    # post_list = Post.objects.order_by("-post_date")
    # user = request.user
    # context = {
    #     'title': 'BILLBOARD',
    #     'posts': post_list,
    #     'user':user,
    # }
    # return render(request, 'mybillboard/index.html', context)
    #return HttpResponse("You are at billboard index.")

def board(request):
    post_list = Post.objects.order_by("-post_date")
    user=request.user
    context = {
        'title': 'BILLBOARD',
        'user': user,
        'posts': post_list,
    }
    return render(request, 'mybillboard/index.html', context)

def add_post(request):
    data = request.POST
    user_name = data["username"]
    subject = data["subject"]
    message = data["message"]
    post_date = datetime.datetime.now()

    p = Post(user_name=user_name, subject=subject, message=message, post_date=post_date)
    p.save()
    return redirect('board')

def user_view(request, user):
    user = request.user.username
    post_list = Post.objects.filter(user_name=user).order_by("-post_date")
    print post_list
    new_user=request.user
    print "lalala " + new_user.username
    context = {
        'title': 'BILLBOARD',
        'user': user,
        'posts': post_list,
    }
    return render(request, 'mybillboard/usermessages.html', context)

def remove_message(request):
    msg_id=request.POST.get("msg-id")
    print msg_id
    msg_to_delete=Post.objects.get(pk=msg_id)
    m=msg_to_delete.delete()
    print m
    new_user = request.user
    print "lalala " + new_user.username
    return JsonResponse({'msg': msg_id+'was deleted'})

    # user = request.user.username
    # post_list = Post.objects.filter(user_name=user).order_by("-post_date")
    # print post_list
    # context = {
    #     'title': 'BILLBOARD',
    #     'user': user,
    #     'posts': post_list,
    # }
    # return render(request, 'mybillboard/usermessages.html', context)

    #return JsonResponse({'msg':msg_id})

def logout_view(request):
    logout(request)
    return redirect("board")

def login_view(request):
    print(request.user.is_authenticated())
    title = 'login'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)  # gets the user itseld
        login(request, user)
        print(request.user.is_authenticated())
        return redirect('board')
    return render(request, 'registration/login.html', {'form': form, 'title': 'BILLBOARD'})

def register_view(request):
    print(request.user.is_authenticated())
    title = 'BILLBOARD'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('board')
    context = {
        'form': form,
        'title': title
    }
    return render(request, 'registration/registration.html', context)