# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_save

from sharp.utls import unique_slug_generator, upload_location


# Create your models here.
class Contact(models.Model):
    en_contact_name = models.CharField(max_length=250)
    ar_contact_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(blank=True, null=True)
    subject = models.CharField(max_length=250, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    replayed = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.en_contact_name

    @property
    def title(self):
        return self.en_contact_name


def pre_save_contact_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_contact_receiver, sender=Contact)
