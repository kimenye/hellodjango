from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('tivi.views',
# 	url(r'^tivi/$', 'index'),
# 	url(r'^tivi/(?P<show_id>\d+)/$', 'detail'),
# )

urlpatterns = patterns('',
	url(r'^tivi/', include('tivi.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^photologue/', include('photologue.urls')),
    url(r'^post/', include('post.urls')),
    url(r'^jmbo/', include('jmbo.urls')),
)