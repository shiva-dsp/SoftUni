# django101.tasks.urls.py

from django.urls import path

from django101.tasks.views import show_bare_minimum_view, show_all_tasks, index

urlpatterns = (
    # http://localhost:8000/tasks/
    path("", index),
    # localhost:8000/tasks/it_works or http://localhost:8000/tasks/it_works
    path("it_works/", show_bare_minimum_view),
    # localhost:8000/tasks/all or http://localhost:8000/tasks/all
    path("all/", show_all_tasks),
    # localhost:8000/tasks/create/
    # path('create/', create),
)