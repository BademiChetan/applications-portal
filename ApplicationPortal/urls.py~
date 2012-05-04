from django.conf.urls.defaults import patterns, include, url
from portal.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^answer$', 'ApplicationPortal.portal.views.answer', name='home'),
    #url(r'^answer$', 'ApplicationPortal.portal.views.answer', name='home'),
    url(r'^core/$', 'ApplicationPortal.portal.views.core_home', name='core'),
    url(r'^coord/$', 'ApplicationPortal.portal.views.coord_home', name='coord'),
    url(r'^register/$', 'ApplicationPortal.portal.views.register', name='register'),
    url(r'^addgroup/(?P<temp>\d+)/$', 'ApplicationPortal.portal.views.addgroup', name='addgroup'),
    url(r'^delgroup/(?P<temp>\d+)/$', 'ApplicationPortal.portal.views.delgroup', name='delgroup'),
    url(r'^editgroup/(?P<temp>\d+)/$', 'ApplicationPortal.portal.views.editgroup', name='editgroup'),
    url(r'^viewapplication/(\d+)/$', 'ApplicationPortal.portal.views.viewapplication', name='viewapplication'),
    url(r'^addevent/$','ApplicationPortal.portal.views.addevent',name='addevent'),
    url(r'^core/(\d+)/$', 'ApplicationPortal.portal.views.viewevent', name='viewevent'),
    url(r'^addquestion/(\d+)/(\d+)/$', core_question_add),
    url(r'^judgementday/$', judgementday),
    url(r'^judgementday/(\d+)/$', judgementday), #Final list of selected candidates
    url(r'^addquestion/(\d+)/(\d+)/$', core_question_add),
    # url(r'^ApplicationPortal/', include('ApplicationPortal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
