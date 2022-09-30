# django101.tasks.urls.py

from django.urls import path

from django101.tasks.views import index

urlpatterns = (
    path("", index),
    # localhost:8000/tasks/create/
    # path('create/', create),
)