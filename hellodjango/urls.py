from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('tivi.views',
	url(r'^tivi/$', 'index'),
	url(r'^tivi/(?P<show_id>\d+)/$', 'detail'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),		
)