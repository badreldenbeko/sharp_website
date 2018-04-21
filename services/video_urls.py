# -*- coding: utf-8 -*-
from django.urls import path

from .views import post_video_delete

app_name = 'services'

urlpatterns = [
    path('<int:pk>/delete/', post_video_delete, name='delete'),
]
