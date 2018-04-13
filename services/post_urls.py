# -*- coding: utf-8 -*-
from django.urls import path

from .views import service_post_detail_update, service_post_delete

app_name = 'services'

urlpatterns = [
    path('<slug:service_slug>/<slug:post_slug>/detail/', service_post_detail_update, name='post_detail_update'),
    path('<slug:post_slug>/delete/', service_post_delete, name='post_delete'),
]
