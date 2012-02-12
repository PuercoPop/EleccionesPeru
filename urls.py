from django.conf.urls.defaults import patterns, include, url

import Elecciones.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Testo.views.home', name='home'),
    # url(r'^Testo/', include('Testo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', Elecciones.views.index),
                       url(r'^seed/$', Elecciones.views.seed),
                       url(r'^crawl/$', Elecciones.views.crawl),
                       url(r'^visualize/$', Elecciones.views.visualize_tree),
                       url(r'^test/$', Elecciones.views.test),
                       url(r'^clean_db/$', Elecciones.views.clean_db),
)
