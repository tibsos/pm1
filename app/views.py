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
def search(request):

    query = request.POST.get('q')

    c = {}

    found_passwords = set(list(Password.objects.filter(user = request.user).filter(title__contains = query)) + list(Password.objects.filter(user = request.user).filter(username__contains = query)) + list(Password.objects.filter(user = request.user).filter(note__contains = query)))

    c['passwords'] = found_passwords

    return render(request, 'components/passwords.html', c)


@lr 
def cancel_search(request):

    return render(request, 'components/passwords.html', {'passwords': Password.objects.filter(user = request.user)})

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
def get_password_info(request, uid):

    password = Password.objects.get(uid = uid)

    c = {}

    c['password'] = password
    c['password_password'] = password.password.decode()

    return render(request, 'components/edit-password.html', c)

@lr
def update_password(request):

    print('f')
    uid = request.POST.get('i')
    print('f')
    
    password_object = Password.objects.get(uid = uid)
    print('f')
    
    password_object.url = request.POST.get('l')
    password_object.title = request.POST.get('t')
    password_object.username = request.POST.get('u')
    password_object.password = request.POST.get('p').encode()
    password_object.note = request.POST.get('n')
    
    print('f')
    password_object.save()

    print('f')

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