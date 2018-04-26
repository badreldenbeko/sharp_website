# -*- coding: utf-8 -*-
from django import forms
from .models import OdooApps


class AppsForm(forms.ModelForm):
    class Meta:
        model = OdooApps
        fields = ['en_app_name', 'ar_app_name', 'app_url', 'image']
