from django.http import HttpResponse, Http404
from django.shortcuts import render

from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

# The render() function takes the request object as its first argument, 
# a template name as its second argument and a dictionary as its optional 
# third argument. It returns an HttpResponse object of the given template 
# rendered with the given context.
    # return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	return render(request, 'polls/detail.html', {'poll': poll})
    	# return HttpResponse("HI")
def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)