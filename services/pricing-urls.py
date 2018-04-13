# -*- coding: utf-8 -*-
from django.urls import path

from .views import service_price_detail, service_price_delete

app_name = 'services'

urlpatterns = [
    path('<slug:slug>/detail/', service_price_detail, name='detail'),
    path('<slug:slug>/delete/', service_price_delete, name='delete'),
]
