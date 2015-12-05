from django.contrib import admin

from .models import Task, Challenge

admin.site.register([Task, Challenge])