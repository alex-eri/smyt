from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('dynamicbase.urls')),
)


from django.conf import settings
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns = patterns('',
                           url(r'^media/(?P<path>.*)$',
                               'django.views.static.serve',{'document_root': settings.MEDIA_ROOT,
                                                            'show_indexes': True}),
                           ) + urlpatterns + staticfiles_urlpatterns()