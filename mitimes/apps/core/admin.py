from django.contrib import admin

from .models import Matter, ActivityType, ActivityCode, Activity, Timesheet


admin.site.register(Matter)
admin.site.register(ActivityType)
admin.site.register(ActivityCode)
admin.site.register(Activity)
admin.site.register(Timesheet)
