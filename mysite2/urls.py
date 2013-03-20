from django.conf.urls import patterns, include, url
from view import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})',hours_ahead),
    # Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^mysite2/', include('mysite2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
