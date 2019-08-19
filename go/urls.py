from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.front.views.inicio', {'ln':0}, name='inicio'),
    url(r'^inicio$', 'app.front.views.inicio', {'ln':0}, name='inicio'),
        url(r'^inicio/(?P<category>[^/]+)$', 'app.front.views.inicio', {'ln':0}, name='inicio'),
    url(r'^nosotros$', 'app.front.views.nosotros', {'ln':0}, name='nosotros'),
        url(r'^nosotros/(?P<category>[^/]+)$', 'app.front.views.nosotros', {'ln':0}, name='nosotros'),        
    url(r'^tramites$', 'app.front.views.tramites_permisos', {'ln':0}, name='tramites_permisos'),
        url(r'^tramites/(?P<category>[^/]+)$', 'app.front.views.tramites_permisos', {'ln':0}, name='tramites_permisos'),
    url(r'^permisos$', 'app.front.views.permisos', name='permisos'),
        url(r'^permisos/(?P<category>[^/]+)$', 'app.front.views.permisos', name='permisos'),
    url(r'^seguros$', 'app.front.views.seguros', {'ln':0}, name='seguros'),        
        url(r'^seguros/(?P<category>[^/]+)$', 'app.front.views.seguros', {'ln':0}, name='seguros'),
    url(r'^auditorias$', 'app.front.views.auditorias', {'ln':0}, name='auditorias'),
        url(r'^auditorias/(?P<category>[^/]+)$', 'app.front.views.auditorias', {'ln':0}, name='auditorias'),
    url(r'^compra_linea$', 'app.front.views.compra_linea', {'ln':0}, name='compra_linea'),
    url(r'^contacto$', 'app.front.views.contacto', {'ln':0}, name='contacto'),

    #   ENGLISH #
    url(r'^home$', 'app.front.views.inicio', {'ln':1}, name='home'),
        url(r'^home/(?P<category>[^/]+)$', 'app.front.views.inicio', {'ln':1}, name='home'),
    url(r'^about-us$', 'app.front.views.nosotros', {'ln':1}, name='about_us'),
        url(r'^about-us/(?P<category>[^/]+)$', 'app.front.views.nosotros', {'ln':1}, name='about_us'),
    url(r'^procedures$', 'app.front.views.tramites_permisos', {'ln':1}, name='tramites_permisos'),
        url(r'^procedures/(?P<category>[^/]+)$', 'app.front.views.tramites_permisos', {'ln':1}, name='tramites_permisos'), 
    url(r'^permits$', 'app.front.views.permisos', {'ln':1}, name='permisos'),
        url(r'^permits/(?P<category>[^/]+)$', 'app.front.views.permisos', {'ln':1}, name='permisos'),
    url(r'^insurance$', 'app.front.views.seguros', {'ln':1}, name='seguros'),
        url(r'^insurance/(?P<category>[^/]+)$', 'app.front.views.seguros', {'ln':1}, name='seguros'),
    url(r'^audits$', 'app.front.views.auditorias', {'ln':1}, name='auditorias'),
        url(r'^audits/(?P<category>[^/]+)$', 'app.front.views.auditorias', {'ln':1}, name='auditorias'),
    url(r'^buy_online$', 'app.front.views.compra_linea', {'ln':1}, name='compra_linea'),
    url(r'^contact$', 'app.front.views.contacto', {'ln':1}, name='contacto'),

    url(r'^send_mail', 'app.front.views.my_send_mail', name='my_send_mail'),



    # url(r'^go/', include('go.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)