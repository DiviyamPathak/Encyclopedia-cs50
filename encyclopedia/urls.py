from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.titentry , name = "entries" ),
    path("", views.search , name = "search")
]
