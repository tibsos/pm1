from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required as lr

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from user.models import Profile
from analytics.models import Funnel

import string
import random

from datetime import datetime as dt
from datetime import timedelta 

import re

def log_in(request):

    c = {}

    c['u'] = request.user

    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        c['m'] = True
    else:
        c['m'] = False

    if request.method == 'POST':

        u = authenticate(

            username = request.POST.get('u').lower(),
            password = request.POST.get('p'),

        )

        if u:

            login(request, u)
            return redirect('/home')

        else: 

            return render(request, 'auth/login.html', {'e': True})
    
    return render(request, 'auth/login.html', c)

def register(request):

    c = {}

    c['u'] = request.user

    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        c['m'] = True
    else:
        c['m'] = False

    if request.method == 'POST':

        name = request.POST.get('n')

        username = request.POST.get('u').lower()
        password = request.POST.get('p')

        user = User(username = username)
        user.set_password(password)
        user.save()

        uid = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))

        while True:
            if Profile.objects.filter(premium_invite_uid = uid).exists():
                uid = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))
            else:
                break

        user.profile.premium_invite_uid = uid
        user.profile.save()

        user = authenticate(username = username, password = password)
        login(request, user)
        

        return redirect('/home')

   

    return render(request, 'auth/register.html', c)

def log_out(request):

    logout(request)

    return redirect('/')

def invited_register(request, premium_invite_uid):

    invited_profile = Profile.objects.filter(premium_invite_uid = premium_invite_uid)

    if invited_profile.invited_friends.all().count() == 2 or not invited_profile.premium:

        return redirect('/register/')

    else:

        if request.method == 'POST':

            name = request.POST.get('n')

            username = request.POST.get('u').lower()
            password = request.POST.get('p')

            user = User(username = username)
            user.set_password(password)
            user.save()

            user.profile.name = name
            user.profile.initials = ''.join(letter[0].upper() for letter in name.split(' '))[0:3]
            user.profile.premium = True
            user.profile.premium_since = dt.now()
            user.profile.premium_until = dt.now() + timedelta(days = 30)

            user.profile.invited_by = invited_profile
            invited_profile.invited_friends.add(user.profile)

            uid = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))

            while True:
                if Profile.objects.get(premium_invite_uid = uid).exists():
                    uid = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(7))
                else:
                    break

            user.profile.premium_invite_uid = uid
            user.profile.save()

            #subject = 'Добро пожаловать в Блокнотик!'
            #message = f'Здравствуйте, {user.profile.name}!\n\nМы рады приветствовать вас у себя на сайте.\n\nЕсли у вас возникнет любой вопрос, пожалуйста, задайте его нам написав по этому адресу.\n\nНу все, пописали!\n\nС уважением,\nКоманда Блокнотика'
            #aemail_from = settings.EMAIL_HOST_USER
            #recipient_list = [user.username]
            #send_mail(subject, message, email_from, recipient_list) 

            user = authenticate(username = username, password = password)
            login(request, user)

            return redirect('/home')
        c = {}

        c['u'] = request.user

        MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

        if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
            c['m'] = True
        else:
            c['m'] = False

        return render(request, 'auth/register.html', c)

def ce(request):

    e = request.POST.get('e')

    if User.objects.filter(username = e).exists():

        return JsonResponse({'u': 'n'})

    else:

        return JsonResponse({'u': 'y'})

@lr
def toggle_mode(request):

    request.user.profile.dark_mode = not request.user.profile.dark_mode
    request.user.profile.save()
    return HttpResponse('K')

""" Account changes """

@lr
def change_name(request):

    request.user.profile.name = request.POST.get('n')

    request.user.profile.initials = ''.join(letter[0].upper() for letter in request.POST.get('n').split(' '))[0:3]

    request.user.profile.save()

    return HttpResponse('K')

@lr
def change_username(request):

    request.user.username = request.POST.get('e')
    
    request.user.save()

    # already exists exception

    return HttpResponse('K')

@lr
def change_password(request):

    user = User(username = request.user.username)
    user.set_password(request.POST.get('p'))
    user.save()

    return HttpResponse('K')

@lr
def cancel_sub(request):

    profile = request.user.profile
    profile.canceled = True
    profile.save()

    return HttpResponse('K')