from django.conf.urls import url

from . import views

app_name = 'maproulette'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^challenge/(?P<challenge_slug>[0-9a-zA-Z\-]+)/task/(?P<task_identifier>[0-9a-zA-Z\-]+)/$', views.task, name='task'),
    url(r'^challenge/(?P<challenge_slug>[0-9a-zA-Z\-]+)/$', views.challenge, name='challenge'),
]
