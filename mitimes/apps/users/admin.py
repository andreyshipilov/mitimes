from django.contrib import admin

from .models import ChargeRate, Client, ContactPhone, ContactEmail, Contact


admin.site.register(ChargeRate)
admin.site.register(Client)
admin.site.register(ContactPhone)
admin.site.register(ContactEmail)
admin.site.register(Contact)