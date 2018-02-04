# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'title': 'BILLBOARD',
    }
    return render(request, 'mybillboard/index.html', context)
    #return HttpResponse("You are at billboard index.")