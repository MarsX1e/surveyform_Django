# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    if 'number' in request.session:
        print'11'
    else:
        request.session['number']=0
    return render(request,'login_app/index.html')
# Create your views here.
def welcome(request):
    request.session['number']+=1
    request.session['name']=request.POST['name']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    request.session['comment']=request.POST['comment']
    contacts={
        'number':request.session['number'],
        'name':request.session['name'],
        'location':request.session['location'],
        'language':request.session['language'],
        'comment':request.session['comment'],
    }
    return render(request,'login_app/hi.html',contacts)
