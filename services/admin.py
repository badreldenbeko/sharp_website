# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Service, ServicePost, ServicePrice


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
