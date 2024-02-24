from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('@dm1n/', admin.site.urls),

    path('', include('user.urls')),
    path('', include('base.urls')),
    path('', include('app.urls')),
    path('', include('analytics.urls')),
    path('', include('blog.urls')),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
