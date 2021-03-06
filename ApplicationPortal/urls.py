from django.conf.urls.defaults import patterns, include, url
#from portal.views import *
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^answer/$', 'ApplicationPortal.portal.views.answer', name='answer'),
    url(r'^register/$', 'ApplicationPortal.portal.views.register', name='register'),
    url(r'^$', 'ApplicationPortal.portal.views.home', name='home'),
    url(r'^logout/$', 'ApplicationPortal.portal.views.log_out', name='logout'),
    url(r'^super_home/$', 'ApplicationPortal.portal.views.super_home', name='super_home'),
    url(r'^addgroup/$', 'ApplicationPortal.portal.views.addgroup', name='addgroup'),
    url(r'^delgroup/(?P<temp>.+)/$', 'ApplicationPortal.portal.views.delgroup', name='delgroup'),
    url(r'^editgroup/(?P<temp>.+)/$', 'ApplicationPortal.portal.views.editgroup', name='editgroup'),
    url(r'^addcore/(?P<temp>.+)/$', 'ApplicationPortal.portal.views.addcore', name='addcore'),
    url(r'^coredetails/(?P<id1>\d+)/$', 'ApplicationPortal.portal.views.coredetails', name='coredetails'),
    url(r'^editcore/(?P<id1>\d+)/$', 'ApplicationPortal.portal.views.editcore', name='editcore'),
    url(r'^core_home/$', 'ApplicationPortal.portal.views.core_home', name='core'),
    url(r'^core_home/addevent/(\d+)/$','ApplicationPortal.portal.views.addevent',name='addevent'),    
    url(r'^core_home/events/(\d+)/$', 'ApplicationPortal.portal.views.core_events', name='events'),
    url(r'^core_home/events/(\d+)/viewapplicants/$', 'ApplicationPortal.portal.views.viewapplicants', name='viewapplicants'),
    url(r'^core_home/events/(\d+)/(\d+)/$', 'ApplicationPortal.portal.views.core_events', name='events_qns'),
    url(r'^core_home/events/(\d+)/final_list/$', 'ApplicationPortal.portal.views.final_list', name='final_list'),
    url(r'^core_home/viewapplication/(\d+)/(\d+)/$', 'ApplicationPortal.portal.views.viewapplication', name='viewapplication'),
    url(r'^core_home/viewapplication/(\d+)/$', 'ApplicationPortal.portal.views.viewapplication', name='viewapplication'),
    
    #url(r'^coord_home/$', 'ApplicationPortal.portal.views.coord_home', name='coord'),

    # Examples:
    # url(r'^ApplicationPortal/', include('ApplicationPortal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
