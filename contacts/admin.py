from django.contrib import admin

from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['en_contact_name', 'email', 'created']
    prepopulated_fields = {'slug': ('en_contact_name',)}


admin.site.register(Contact, ContactAdmin)
