from django.contrib import admin

from .models import ChargeRate, Client, ContactPhone, ContactEmail, Contact, \
                    Profile
from core.models import ActivityCode


admin.site.register(ChargeRate)
admin.site.register(Client)
admin.site.register(ContactPhone)
admin.site.register(ContactEmail)
admin.site.register(Contact)

class ChargeRateInline(admin.TabularInline):
    model = ChargeRate

class ActivityCodeInline(admin.TabularInline):
    model = ActivityCode

class ProfileAdmin(admin.ModelAdmin):
    inlines = (ChargeRateInline, ActivityCodeInline,)
admin.site.register(Profile, ProfileAdmin)