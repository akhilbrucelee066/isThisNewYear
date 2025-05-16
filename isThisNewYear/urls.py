from django.urls import path

from . import views

urlpatterns = [
    path("<int:simulate>", views.index, name='index'),
    path("", views.index, name='index'),
]