# -*- coding: utf-8 -*-
from django.urls import path

from .views import service_post_comment_delete

app_name = 'services'

urlpatterns = [
    path('<int:pk>/delete/', service_post_comment_delete, name='comment_delete'),
]
