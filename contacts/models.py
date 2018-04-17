# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_save

from sharp.utls import unique_slug_generator


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def title(self):
        return self.name


def pre_save_contact_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_contact_receiver, sender=Contact)
