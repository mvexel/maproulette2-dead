from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import logout
from .models import Challenge, Task

def index(request):
    challenge_list = Challenge.objects.order_by('name')[:5]
    context = {'challenge_list': challenge_list}
    return render(request, 'maproulette/index.html', context)


def task(request, challenge_slug, task_identifier):
    task = get_object_or_404(
    	Task,
        challenge=challenge_slug,
        pk=task_identifier)
    return render(
        request,
        'maproulette/task.html',
        {
            'task': task,
        })

def challenge(request, challenge_slug):
    challenge = get_object_or_404(
        Challenge,
        pk=challenge_slug)
    return render(
        request,
        'maproulette/challenge.html',
        {
            'challenge': challenge,
        })

def signout(request):
    logout(request)
    return redirect('/')

def signin(request):
    logout(request)
    return redirect('/')