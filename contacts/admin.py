from django.contrib import admin

from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['name', 'email', 'created']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Contact, ContactAdmin)
