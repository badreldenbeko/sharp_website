# -*- coding: utf-8 -*-
from django.urls import path

from .views import contact_list

app_name = 'contacts'

urlpatterns = [
    path('', contact_list, name='list'),
]
