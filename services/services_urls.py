# -*- coding: utf-8 -*-
from django.urls import path

from .views import service_list_create, service_detail_update, service_delete

app_name = 'services'

urlpatterns = [
    path('<slug:slug>/detail/', service_detail_update, name='detail'),
    path('<slug:slug>/delete/', service_delete, name='delete'),
    path('', service_list_create, name='list_create'),
]
