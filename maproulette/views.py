from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Challenge, Task

def index(request):
	challenge_list = Challenge.objects.order_by('name')[:5]
	context = {'challenge_list': challenge_list}
	return render(request, 'maproulette/index.html', context)


def task(request, task_identifier):
    try:
        task = Task.objects.get(pk=task_identifier)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    return render(request, 'maproulette/task.html', {'task_identifier': task_identifier})

def challenge(request, challenge_slug):
	return HttpResponse("This is challenge {}".format(challenge_slug))