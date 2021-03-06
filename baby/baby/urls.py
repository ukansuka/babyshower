from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lista.views.home', name='home'),
    # url(r'^baby/', include('baby.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
        ),

    url(r'^home/$','lista.views.home'),
    url(r'^regalo/$','lista.views.one_regalo'),
    url(r'^regalo/(\d+)$','lista.views.one_regalo'),
    url(r'^mensajerecibido/(\d+)$','lista.views.mensajerecibido'),

)
