from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def index(request):
    posts = Post.objects.filter(status="p").order_by("-published_date")
    return render(request, "index.html", {"posts": posts})


def test(request):
    return render(request, "blog_index.html")
