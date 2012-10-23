from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api

from .api import ActivityResource, ClientResource, MatterResource, ContactResource, ContactEmailResource


admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(ClientResource())
v1_api.register(ActivityResource())
v1_api.register(MatterResource())
v1_api.register(ContactResource())
v1_api.register(ContactEmailResource())

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
