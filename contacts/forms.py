# -*- coding: utf-8 -*-
from django import forms

from .models import Contact


class ContactForm(forms.Form):
    en_contact_name = forms.CharField(max_length=250)
    phone = forms.CharField(max_length=11)
    email = forms.EmailField()
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['en_contact_name', 'ar_contact_name', 'email', 'replayed', 'image']
