from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import json

from django.contrib.auth.decorators import login_required as lr

from datetime import datetime as dt
from datetime import timedelta
import datetime

from django.contrib.auth.models import User

from .models import *

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


""" APP """
@lr
def app(request):
    
    c = {}
    
    c['passwords'] = Password.objects.filter(user = request.user)

    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

    # Check if the User-Agent contains a string that is common for mobile devices
    is_mobile = 'mobile' in user_agent or 'android' in user_agent or 'iphone' in user_agent

    if is_mobile:

        return render(request, 'home_mobile.html', c)

    else: 

        return render(request, 'home.html', c)
    
@lr
def create_password(request):
    
    url = request.POST.get('l')
    title = request.POST.get('t')
    username = request.POST.get('u')
    password = request.POST.get('p').encode('utf-8')
    note = request.POST.get('n')
    
    Password.objects.create(
        
        user = request.user,
        url = url,
        title = title,
        username = username,
        password = password,
        note = note
        
    )
    
    passwords = Password.objects.filter(user = request.user)
    
    return render(request, 'components/passwords.html', {'passwords': passwords})

@lr
def update_password(request):
    
    uid = request.POST.get('i')
    password_object = Password.objects.get(uid = uid)
    
    url = request.POST.get('l')
    title = request.POST.get('t')
    username = request.POST.get('u')
    password = request.POST.get('p').encode('utf-8')
    note = request.POST.get('n')
    
    password_object.url = url
    password_object.title = title
    password_object.username = username
    password_object.password = password
    password_object.note = note
    
    return HttpResponse('K')

@lr
def delete_password(request):
    
    uid = request.POST.get('i')
    
    password = Password.objects.get(uid = uid)
    password.delete()
    
    return HttpResponse('K')

@lr
def search_notes(request):

    c = {}

    query = request.POST.get('q')

    notes1 = list(Note.objects.filter(author = request.user).filter(deleted = False).filter(archived = False).filter(title__contains = query))

    return render(request, 'components/notes.html', c)