from django import http
from django.shortcuts import render

from django101.tasks.models import Task


# django101.tasks.views.py


def show_bare_minimum_view(request):
    return http.HttpResponse('It works ...')


def show_all_tasks(request):
    all_tasks = Task.objects.order_by("id").all()
    # [name(id), name(id)]
    result = ", ".join(f"{t.name}({t.id})" for t in all_tasks)

    return http.HttpResponse(result)


def index(request):
    context = {
        "title": "The tasks app!",
    }
    return render(request, "index.html", context)