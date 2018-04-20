# -*- coding: utf-8 -*-
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Service, ServiceClient, ServicePost, ServicePostComment, ServicePrice


class ServiceForm(forms.ModelForm):
    en_description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Service
        fields = ['en_name', 'ar_name', 'en_description', 'ar_description', 'image', 'publish_on_home',
                  'publish_pricing']


class ServiceClientForm(forms.ModelForm):
    class Meta:
        model = ServiceClient
        fields = ['en_client_name', 'ar_client_name', 'logo']


class ServicePostForm(forms.ModelForm):
    class Meta:
        model = ServicePost
        fields = ['en_title', 'ar_title', 'en_body', 'ar_body', 'image']


class ServicePostCommentForm(forms.ModelForm):
    class Meta:
        model = ServicePostComment
        fields = ['name', 'email', 'comment']


class ServicePriceForm(forms.ModelForm):
    class Meta:
        model = ServicePrice
        fields = ['en_price_title', 'ar_price_title', 'price', 'en_detail', 'ar_detail']
