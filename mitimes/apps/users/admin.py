from django.contrib import admin

from .models import ChargeRate, Client, ContactPhone, ContactEmail, Contact, \
                    Profile


admin.site.register(ChargeRate)
admin.site.register(Client)
admin.site.register(ContactPhone)
admin.site.register(ContactEmail)
admin.site.register(Contact)
admin.site.register(Profile)