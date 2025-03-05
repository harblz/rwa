from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r"^test/", views.test, name="test"),
]
