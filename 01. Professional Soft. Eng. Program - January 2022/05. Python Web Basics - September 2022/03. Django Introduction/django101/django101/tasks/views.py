from django import http
from django.shortcuts import render

# django101.tasks.views.py


def index(request):
    return http.HttpResponse('It works ...')