from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Challenge, Task

def index(request):
	challenge_list = Challenge.objects.order_by('name')[:5]
	context = {'challenge_list': challenge_list}
	return render(request, 'maproulette/index.html', context)


def task(request, challenge_slug, task_identifier):
    try:
        task = Task.objects.get(
        	challenge=challenge_slug,
        	pk=task_identifier)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(
    	request,
    	'maproulette/task.html',
    	{
    		'challenge_slug': challenge_slug,
    		'task_identifier': task_identifier
    	})

def challenge(request, challenge_slug):
    try:
        task = Challenge.objects.get(
        	pk=challenge_slug)
    except Challenge.DoesNotExist:
        raise Http404("Challenge does not exist")
    return render(
    	request,
    	'maproulette/challenge.html',
    	{
    		'challenge_slug': challenge_slug,
    	})
