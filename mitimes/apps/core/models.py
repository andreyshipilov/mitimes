from django.db import models

from users.models import Client, Profile


class Matter(models.Model):
    key = models.CharField(max_length=100,)
    description = models.CharField(max_length=300,)
    client = models.ForeignKey(Client,)

    def __unicode__(self):
        return "%s (%s)" % (self.description, self.key)

class ActivityType(models.Model):
    title = models.CharField(max_length=50, unique=True,)

    def __unicode__(self):
        return self.title

class ActivityCode(models.Model):
    profile = models.ForeignKey(Profile,)
    description = models.CharField(max_length=100,)
    is_default_for_call_to = models.BooleanField(default=False,)
    is_default_for_call_from = models.BooleanField(default=False,)
    is_default_for_email_to = models.BooleanField(default=False,)
    is_default_for_email_from = models.BooleanField(default=False,)
    is_default_for_event = models.BooleanField(default=False,)

    def __unicode__(self):
        return self.description

class Activity(models.Model):
    profile = models.ForeignKey(Profile,)
    type = models.ForeignKey(ActivityType,)
    code = models.ForeignKey(ActivityCode,)
    date_time = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True,)
    matter = models.ForeignKey(Matter,)
    units = models.PositiveIntegerField(default=0,)
    description = models.CharField(max_length=200, blank=True,)
    is_active = models.BooleanField(default=True,)
    is_autogenerated = models.BooleanField(default=True, editable=False,)
    is_on_current_timesheet = models.BooleanField(default=True,)
    timesheet = models.ForeignKey("Timesheet", blank=True, null=True,)

    class Meta:
        verbose_name_plural = 'activities'

    def __unicode__(self):
        if self.description:
            return "%s: %s (%s)" % (self.type, self.description,
                                    self.matter.key)
        return "%s: %s (%s)" % (self.type, self.code, self.matter)

    def save(self, *args, **kwargs):
        """
        Overrides 'is_on_current_timesheet' to be False if 'timesheet' is set.
        """
        self.is_on_current_timesheet = False if self.timesheet else True
        models.Model.save(self, *args, **kwargs)

    @staticmethod
    def get_on_current_timesheet(profile):
        """
        Returns all activities on current timesheet,
        not posted for current profile.
        """
        return Activity.objects.filter(profile=profile,
                                       is_on_current_timesheet=True)

    @staticmethod
    def remove_all(profile):
        """
        Removes all activities not on current timesheet,
        not posted for current profile.
        """
        Activity.objects.filter(profile=profile, is_on_current_timesheet=False,
                                timesheet_isnull=True,) \
                        .update(is_active=False,)

class Timesheet(models.Model):
    date_posted = models.DateTimeField(auto_now=True,)
    is_emailed = models.BooleanField(default=False,)

    def __unicode__(self):
        return str(self.date_posted)

    def get_not_emailed(self):
        """
        Returns all posted timesheets.
        """
        return self.objects.filter(is_emailed=False)
