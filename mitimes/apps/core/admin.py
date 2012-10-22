from django.contrib import admin

from .models import Matter, ActivityType, ActivityCode, Activity


admin.site.register(Matter)
admin.site.register(ActivityType)
admin.site.register(ActivityCode)
admin.site.register(Activity)