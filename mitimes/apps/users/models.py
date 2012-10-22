from django.db import models


class ChargeRate(models.Model):
    is_default = models.BooleanField(default=False,)
    description = models.CharField(max_length=100,)
    per_hour = models.DecimalField(max_digits=10, decimal_places=2,)
    
    def __unicode__(self):
        return "%s, $%s per hour" % (self.description, self.per_hour)

    def get_rate_per_unit(self):
        return 

class Client(models.Model):
    first_name = models.CharField(max_length=50,)
    last_name = models.CharField(max_length=50,)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

class ContactPhone(models.Model):
    phone = models.CharField(max_length=20,)

    def __unicode__(self):
        return self.phone

class ContactEmail(models.Model):
    email = models.EmailField(max_length=300,)

    def __unicode__(self):
        return self.email

class Contact(models.Model):
    is_active = models.BooleanField(default=True,)
    charge_rate = models.ForeignKey(ChargeRate,)
    default_name = models.CharField(max_length=200,)
    first_name = models.CharField(max_length=50, blank=True,)
    last_name = models.CharField(max_length=50, blank=True,)
    phones = models.ForeignKey(ContactPhone, blank=True,)
    email = models.ForeignKey(ContactEmail, blank=True,)
    
    def __unicode__(self):
        if self.first_name or self.last_name:
            if self.last_name:
                return "%s %s" % (self.first_name, self.last_name)
            return self.first_name
        return self.default_name
