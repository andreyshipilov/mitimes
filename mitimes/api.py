"""
Actions to implement.

#activity.remove - done through ORM
activity.charge
activity.set 
#activity.get - done
#activities.get - done
#activities_before.get - done
#activities.remove_all - done through ORM

contact.ignore
contacts.search - done
contacts.set

#matters.search - done

timesheet.post - done
timesheet.get - done
timesheet.email

timer.set
"""

from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from core.models import Matter, ActivityType, ActivityCode, Activity, Timesheet
from users.models import Client, Profile, Contact, ContactEmail, ContactPhone


class ProfileResource(ModelResource):
    class Meta:
        queryset = Profile.objects.all()

class ActivityResource(ModelResource):
    class Meta:
        include_resource_uri = False
        queryset = Activity.objects.all()
        authentication = SessionAuthentication()
        authorization = Authorization()
        allowed_methods = ('get', 'post',)

    def obj_get_list(self, request=None, **kwargs):
        return Activity.get_active_for_user(user=request.user)

    def obj_create(self, bundle, request=None, **kwargs):
        return super(ActivityResource, self).obj_create(self, bundle,
                                                        request, **kwargs)

class MatterResource(ModelResource):
    class Meta:
        queryset = Matter.objects.all()
        include_resource_uri = False
        authentication = SessionAuthentication()
        authorization = Authorization()
        allowed_methods = ('get',)
        
    def obj_get_list(self, request=None, **kwargs):
        return Matter.get_for_user(request.user)

class ClientResource(ModelResource):
    class Meta:
        queryset = Client.objects.all()
        authentication = SessionAuthentication()
        authorization = Authorization()
        allowed_methods = ('get', 'post',)


class ContactResource(ModelResource):
    emails = fields.ToManyField('mitimes.api.ContactEmailResource', 'emails', related_name='contact', full=True,)
    phones = fields.ToManyField('mitimes.api.ContactPhoneResource', 'phones', related_name='contact', full=True,)
    
    class Meta:
        queryset = Contact.objects.all()
        include_resource_uri = False
        authentication = SessionAuthentication()
        authorization = Authorization()
        allowed_methods = ('get',)

class ContactEmailResource(ModelResource):
    class Meta:
        queryset = ContactEmail.objects.all()
        include_resource_uri = False

class ContactPhoneResource(ModelResource):
    class Meta:
        queryset = ContactPhone.objects.all()
        include_resource_uri = False
