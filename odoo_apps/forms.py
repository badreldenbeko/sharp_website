# -*- coding: utf-8 -*-
from django import forms
from .models import OdooApps


class AppsForm(forms.ModelForm):
    class Meta:
        model = OdooApps
        fields = ['ar_app_name', 'en_app_name', 'app_url', 'image']
