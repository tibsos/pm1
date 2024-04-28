from django.shortcuts import render, HttpResponse

from user.models import Profile
from analytics.models import Funnel

from django.utils import timezone
from .utils import get_ip_country_city


def overview(request):

    if request.user.username == '_':

        c = {}

        c['users'] = Profile.objects.all().count()
        c['premium_users'] = Profile.objects.all().filter(premium = True).count()
        c['revenue'] = Profile.objects.all().filter(premium = True).count() * 97

        c['notepads'] = Folder.objects.all().count()
        c['notes'] = Note.objects.all().count()

        # page visits
        c['landing_visits'] = Funnel.objects.filter(url = 'https://bloknot-ik.ru/').count()
        c['register_visits'] = Funnel.objects.filter(url = 'https://bloknot-ik.ru/register/').count()
        c['login_visits'] = Funnel.objects.filter(url = 'https://bloknot-ik.ru/login/').count()
        c['home_visits'] = Funnel.objects.filter(url = 'https://bloknot-ik.ru/home/').count()

        return render(request, 'overview.html', c)

def funnel(request):

    if request.method == 'POST':

        url = request.META.get('HTTP_REFERER')
        ip = request.META.get('REMOTE_ADDR')

        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()

        # Check if the user agent contains keywords indicative of a mobile device
        mobile = any(keyword in user_agent for keyword in ['mobile', 'android', 'iphone', 'ipad'])

        ip, country, city = get_ip_country_city(request)
        
        Funnel.objects.create(

            url = url,
            ip = ip,
            country = country,
            city = city,
            mobile = mobile,
            entered_at = timezone.now()

        )

        return HttpResponse('K')