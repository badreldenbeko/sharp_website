# -*- coding: utf-8 -*-
from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class ContactReplayForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['replayed']