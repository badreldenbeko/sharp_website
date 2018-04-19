# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from ckeditor.fields import RichTextField
from sharp.utls import unique_slug_generator, upload_location


# Create your models here.
class Service(models.Model):
    en_name = models.CharField(max_length=200)
    ar_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    en_description = RichTextField(null=True, blank=True)
    ar_description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    publish_on_home = models.BooleanField(default=False)
    publish_pricing = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.en_name

    @property
    def title(self):
        return self.en_name

    def get_absolute_url(self):
        return reverse('service:detail', kwargs={'slug': self.slug})


def pre_save_service_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_service_receiver, sender=Service)


class ServicePost(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='posts')
    en_title = models.CharField(max_length=200)
    ar_title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    en_body = RichTextField(null=True, blank=True)
    ar_body = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.en_title

    @property
    def title(self):
        return self.en_title

    def get_absolute_url(self):
        return reverse('post:post_detail_update', kwargs={'service_slug': self.service.slug, 'post_slug': self.slug})


def pre_save_service_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_service_post_receiver, sender=ServicePost)


class ServicePrice(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='prices')
    en_price_title = models.CharField(max_length=200)
    ar_price_title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    en_detail = RichTextField(null=True, blank=True)
    ar_detail = RichTextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.en_price_title

    @property
    def title(self):
        return self.en_price_title

    def get_absolute_url(self):
        return reverse('price:detail', kwargs={'slug': self.slug})


def pre_save_service_price_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_service_price_receiver, sender=ServicePrice)
