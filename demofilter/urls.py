from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'posts.views.index'),
     url(r'^create/', 'posts.views.create'),

    # Examples:
    # url(r'^$', 'demofilter.views.home', name='home'),
    # url(r'^demofilter/', include('demofilter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
