# -*- coding: utf-8 -*-
from django.urls import path
from .views import app_list

app_name = 'odoo_apps'


urlpatterns = [
    path('', app_list, name='list'),
]
