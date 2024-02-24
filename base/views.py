from django.shortcuts import render, HttpResponse

from .models import Message
from analytics.models import Funnel      

import re

# Landing
def l(request):

    c = {}

    c['u'] = request.user

    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        c['m'] = True
    else:
        c['m'] = False

    return render(request, 'landing.html', c)

# Info
def t(request):
    return render(request, 'info/terms.html', {'u': request.user})

def p(request):
    return render(request, 'info/privacy.html', {'u': request.user})

def j(request):
    return render(request, 'info/juridical.html', {'u': request.user})

# Contact
def c(request):

    c = {}

    c['u'] = request.user

    MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        c['m'] = True
    else:
        c['m'] = False

    return render(request, 'contact.html', c)
    
# contact submit
def cs(request):
    
    if request.user.is_authenticated:
        
        Message.objects.create(
            
            user = request.user,

            topic = request.POST.get('t'),
            message = request.POST.get('m'),
            
        )
        
    else:
        
        Message.objects.create(
            
            name = request.POST.get('n'),
            email = request.POST.get('e'),
            
            topic = request.POST.get('t'),
            message = request.POST.get('m'),

        )
    
    return HttpResponse('K')