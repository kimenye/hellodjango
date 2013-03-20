# Create your views here.
# from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from tivi.models import Show
# from django.http import HttpResponse

def index(request):
    latest_poll_list = Show.objects.all()[:5]
    # t = loader.get_template('tivi/index.html')
    # c = Context({
        # 'latest_poll_list': latest_poll_list,
    # })
    # return HttpResponse(t.render(c))
	# return HttpResponse("Hello world, you are looking at the tivi index")
    return render_to_response('tivi/index.html', {'latest_poll_list': latest_poll_list})

from django.http import Http404
def detail(request, show_id):
	s = get_object_or_404(Show, pk=show_id)
	return render_to_response('tivi/detail.html', {'show': s})    	

