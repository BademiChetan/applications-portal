from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ApplicationPortal.portal.views.home', name='home'),
    url(r'^core/$', 'ApplicationPortal.portal.views.core_home', name='core'),
    url(r'^coord/$', 'ApplicationPortal.portal.views.coord_home', name='coord'),
    url(r'^register/$', 'ApplicationPortal.portal.views.register', name='register'),
    url(r'^addgroup/(?P<temp>\d+)/$', 'ApplicationPortal.portal.views.addgroup', name='addgroup'),
    url(r'^delgroup/(?P<temp>\d+)/$', 'ApplicationPortal.portal.views.delgroup', name='delgroup'),
    url(r'^editgroup/(?P<temp>\d+)/$', 'ApplicationPortal.portal.views.editgroup', name='editgroup'),

    url(r'^viewapplication/(?P<temp>([A-Z a-z]))/$', 'ApplicationPortal.portal.views.viewapplication', name='viewapplication'),

    url(r'^core/viewevent/$', 'ApplicationPortal.portal.views.viewevent', name='viewevent'),

    # url(r'^ApplicationPortal/', include('ApplicationPortal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
