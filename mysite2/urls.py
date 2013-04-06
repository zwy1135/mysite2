from django.conf.urls import patterns, include, url
#import view
#from contact.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mysite2.view',
    url('^time/$','current_datetime'),
    url(r'^time/plus/(\d{1,2})','hours_ahead'),
    url('^meta/$','display_meta'),
    url('^search/$','search'),
    
    # Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^mysite2/', include('mysite2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('mysite2.contact.views',
    url('contact/$','contact'),
    )
