from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [

    path('blog', blog, name = 'blog'),
    path('blog/<slug:slug>', post, name = 'post'),

]