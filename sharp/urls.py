# -*- coding: utf-8 -*-
"""sharp_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf import settings
# from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, LogoutView
from django.urls import path, include

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('rosetta/', include('rosetta.urls')),
    path('services/', include('services.services_urls', namespace='service')),
    path('post/', include('services.post_urls', namespace='post')),
    path('comment/', include('services.comment_urls', namespace='comment')),
    path('price/', include('services.pricing-urls', namespace='price')),
    path('contact/', include('contacts.urls', namespace='contact')),
    path('video/', include('services.video_urls', namespace='video')),
    path('client/', include('services.clients_urls', namespace='client')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('home.urls', namespace='home')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
