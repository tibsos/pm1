from django.urls import path, include

from .views import *

app_name = 'app'

urlpatterns = [
    
    path('home', app, name = 'app'),

]

htmx_urlpatterns = [

    path('cp', create_password, name = 'create-password'),

]

ajax_urlpatterns = [

    path('gpi/<uuid:uid>', get_password_info, name = 'get-password-info'),
    path('dp', delete_password, name = 'delete-password'),
    path('up/<uuid:uid>', update_password, name = 'update-password'),

]

urlpatterns += htmx_urlpatterns
urlpatterns += ajax_urlpatterns