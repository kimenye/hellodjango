from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from tivi.models import Show

urlpatterns = patterns('tivi.views',
	# url(r'^$', 'index'),
	url(r'^$',
        ListView.as_view(
            queryset=Show.objects.all()[:5],
            context_object_name='latest_poll_list',
            template_name='tivi/index.html')),

	# url(r'^(?P<show_id>\d+)/$', 'detail'),
	url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Show,
            template_name='tivi/detail.html')),
)