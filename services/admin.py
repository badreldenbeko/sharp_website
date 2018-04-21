# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Service, ServiceClient, ServicePost, ServicePostVideo, ServicePrice


# Register your models here.
class ServicePostAdmin(admin.ModelAdmin):
    model = ServicePost
    prepopulated_fields = {'slug': ('en_title',)}


admin.site.register(ServicePost, ServicePostAdmin)


class ServicesAdmin(admin.ModelAdmin):
    model = ServicePost
    prepopulated_fields = {'slug': ('en_name',)}


admin.site.register(Service, ServicesAdmin)


class ServicePriceAdmin(admin.ModelAdmin):
    model = ServicePrice
    prepopulated_fields = {'slug': ('en_price_title',)}


admin.site.register(ServicePrice, ServicePriceAdmin)


admin.site.register(ServicePostVideo)


admin.site.register(ServiceClient)
