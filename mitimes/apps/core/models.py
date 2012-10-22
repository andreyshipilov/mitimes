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
    description = models.CharField(max_length=100,)
    is_default_for_call_to = models.BooleanField(default=False,)
    is_default_for_call_from = models.BooleanField(default=False,)
    is_default_for_email_to = models.BooleanField(default=False,)
    is_default_for_email_from = models.BooleanField(default=False,)
    is_default_for_event = models.BooleanField(default=False,)

    def __unicode__(self):
        return self.description

class Activity(models.Model):
    user = models.ForeignKey(Profile,)
    type = models.ForeignKey(ActivityType,)
    code = models.ForeignKey(ActivityCode,)
    date_time = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True,)
    matter = models.ForeignKey(Matter,)
    units = models.PositiveIntegerField(default=0,)
    description = models.CharField(max_length=200, blank=True,)

    class Meta:
        verbose_name_plural = 'activities'

    def __unicode__(self):
        if self.description:
            return "%s: %s (%s)" % (self.type, self.description,
                                    self.matter.key)
        return "%s: %s (%s)" % (self.type, self.code, self.matter)
