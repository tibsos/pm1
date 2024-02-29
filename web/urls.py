from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {

    'posts': PostSitemap,

}

urlpatterns = [

    path('@dm1n/', admin.site.urls),

    path('', include('user.urls')),
    path('', include('base.urls')),
    path('', include('blog.urls')),
    path('', include('app.urls')),
    path('', include('analytics.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name ='django.contrib.sitemaps.views.sitemap')


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
