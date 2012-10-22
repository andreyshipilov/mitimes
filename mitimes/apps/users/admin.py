from django.contrib import admin

from .models import ChargeRate, Client, ContactPhone, ContactEmail, Contact, \
                    Profile


admin.site.register(ChargeRate)
admin.site.register(Client)
admin.site.register(ContactPhone)
admin.site.register(ContactEmail)
admin.site.register(Contact)

class ChargeRateInline(admin.TabularInline):
    model = ChargeRate

class ProfileAdmin(admin.ModelAdmin):
    inlines = (ChargeRateInline,)
admin.site.register(Profile, ProfileAdmin)