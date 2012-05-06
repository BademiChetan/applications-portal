from django.conf.urls.defaults import patterns, include, url
#from portal.views import *
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^answer/$', 'ApplicationPortal.portal.views.answer', name='answer'),
    #url(r'^answer$', 'ApplicationPortal.portal.views.answer', name='home'),
    url(r'^core/$', 'ApplicationPortal.portal.views.core_home', name='core'),
    url(r'^coord/$', 'ApplicationPortal.portal.views.coord_home', name='coord'),
    url(r'^$', 'ApplicationPortal.portal.views.home', name='home'),
    #url(r'^core/$', 'ApplicationPortal.portal.views.core_home', name='core'),
    #url(r'^coord/$', 'ApplicationPortal.portal.views.coord_home', name='coord'),
    url(r'^register/$', 'ApplicationPortal.portal.views.register', name='register'),
    url(r'^logout/$', 'ApplicationPortal.portal.views.log_out', name='logout'),
    #url(r'^viewapplication/(\d+)/$', 'ApplicationPortal.portal.views.viewapplication', name='viewapplication'),
    #url(r'^addevent/$','ApplicationPortal.portal.views.addevent',name='addevent'),
    #url(r'^core/(\d+)/$', 'ApplicationPortal.portal.views.viewevent', name='viewevent'),
    #url(r'^addquestion/(\d+)/(\d+)/$', core_question_add),
    #url(r'^judgementday/$', judgementday),
    #url(r'^judgementday/(\d+)/$', judgementday), #Final list of selected candidates
    #url(r'^addquestion/(\d+)/(\d+)/$', core_question_add),
    #url(r'^editquestion/(\d+)/$','ApplicationPortal.portal.views.editquestion',name='editquestion'),
    url(r'^super_home/$', 'ApplicationPortal.portal.views.super_home', name='super_home'),
    url(r'^addgroup/$', 'ApplicationPortal.portal.views.addgroup', name='addgroup'),
    url(r'^delgroup/(?P<temp>.+)/$', 'ApplicationPortal.portal.views.delgroup', name='delgroup'),
    url(r'^editgroup/(?P<temp>.+)/$', 'ApplicationPortal.portal.views.editgroup', name='editgroup'),
    url(r'^addcore/(?P<temp>.+)/$', 'ApplicationPortal.portal.views.addcore', name='addcore'),
    url(r'^coredetails/(?P<id1>\d+)/$', 'ApplicationPortal.portal.views.coredetails', name='coredetails'),

    # url(r'^ApplicationPortal/', include('ApplicationPortal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
