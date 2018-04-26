# -*- coding: utf-8 -*-
from django.urls import path
from .views import app_list, app_update, app_delete

app_name = 'odoo_apps'

urlpatterns = [
    path('<slug:slug>/update', app_update, name='update'),
    path('<slug:slug>/delete', app_delete, name='delete'),
    path('', app_list, name='list'),
]
