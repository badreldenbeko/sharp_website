# -*- coding: utf-8 -*-
from django.urls import path

from .views import contact_list, contact_delete, contact_edit

app_name = 'contacts'

urlpatterns = [
    path('<slug:slug>/delete/', contact_delete, name='delete'),
    path('<slug:slug>/edit/', contact_edit, name='edit'),
    path('', contact_list, name='list'),
]
