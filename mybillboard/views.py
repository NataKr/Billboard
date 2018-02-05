# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

def index(request):
    post_list = Post.objects.all()
    context = {
        'title': 'BILLBOARD',
        'posts': post_list,
    }
    return render(request, 'mybillboard/index.html', context)
    #return HttpResponse("You are at billboard index.")

def board(request, user_name):
    post_list=Post.objects.all()
    logged_user=user_name
    context = {
        'title': 'BILLBOARD',
        'logged_user': logged_user,
        'posts': post_list,
    }
    return render(request, 'mybillboard/board.html', context)

