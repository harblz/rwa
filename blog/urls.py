from django.urls import path, re_path

from . import views

urlpatterns = [
    path("<str:slug>/", views.post, name="post"),
    path("test/", views.test, name="test"),
]
