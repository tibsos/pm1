from django.urls import path

from .views import *

app_name = 'analytics'

urlpatterns = [

    path('@N@L/', overview),
    path('funnel/', funnel, name = 'funnel'),

]