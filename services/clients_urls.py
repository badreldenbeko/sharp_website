# -*- coding: utf-8 -*-
from django.urls import path

from .views import service_client_delete

app_name = 'services'

urlpatterns = [
    path('<int:pk>/delete/', service_client_delete, name='delete'),
]
