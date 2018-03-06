# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

# Create your views here.

def dashboard(request):
    if 'email' not in request.session:
        request.session.flush()
        return redirect('/')
    else:
        context = {
            'curUserName' : request.session['name'],
            'curUser' : User.objects.get(id = request.session['curuserid']),
            'otherUser': User.objects.all().exclude(friends = request.session['curuserid']).exclude( id = request.session['curuserid'])
        }
        
        return render(request, 'friends_app/index.html', context)

def add(request, id):
    if 'email' not in request.session:
        request.session.flush()
        return redirect('/')
    else:
        newfriend = User.objects.get(id = request.session['curuserid'])
        newfriend.friends.add(User.objects.get(id = id))
        messages.success(request, 'Friend has been added')
        return redirect('/friends/dashboard')

def remove(request, id):
    if 'email' not in request.session:
        request.session.flush()
        return redirect('/')
    else:
        newfriend = User.objects.get(id = request.session['curuserid'])
        newfriend.friends.remove(User.objects.get(id = id))
        messages.success(request, 'Friend has been removed')
        return redirect('/friends/dashboard')

def show(request, id):
    if 'email' not in request.session:
        request.session.flush()
        return redirect('/')
    else:
        context = {
            'otherUser' : User.objects.get(id = id),
        }
        return render(request, 'friends_app/profile.html', context)

