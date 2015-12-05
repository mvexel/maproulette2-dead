from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Challenge

def index(request):
	challenge_list = Challenge.objects.order_by('name')[:5]
	template = loader.get_template('maproulette/index.html')
	context = RequestContext(request, {
        'challenge_list': challenge_list,
    })
	return HttpResponse(template.render(context))


def task(request, task_identifier):
	return HttpResponse("This is task {}".format(task_identifier))


def challenge(request, challenge_slug):
	return HttpResponse("This is challenge {}".format(challenge_slug))