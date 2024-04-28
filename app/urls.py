from django.urls import path, include

from .views import *

app_name = 'app'

urlpatterns = [
    
    path('home', app, name = 'app'),
    
    path('cp', create_password, name = 'create-password'),
    path('up', update_password, name = 'update-password'),
    path('dp', delete_password, name = 'delete-password'),
    
]
