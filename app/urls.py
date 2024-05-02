from django.urls import path, include

from .views import *

app_name = 'app'

urlpatterns = [
    
    path('home', app, name = 'app'),

]

htmx_urlpatterns = [

    path('cp', create_password, name = 'create-password'),
    path('gpi/<uuid:uid>', get_password_info, name = 'get-password-info'),

    path('s', search, name = 'search'),
    path('cs', cancel_search, name = 'cancel-search'),

]

ajax_urlpatterns = [

    path('dp', delete_password, name = 'delete-password'),
    path('up', update_password, name = 'update-password'),

]

urlpatterns += htmx_urlpatterns
urlpatterns += ajax_urlpatterns