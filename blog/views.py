from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def index(request):
    posts = Post.objects.filter(status="p").order_by("-published_date")
    return render(request, "index.html", {"posts": posts})


def test(request):
    return render(request, "blog/blog_index.html")


def post(request, slug):
    post_obj = Post.objects.get(slug=slug)
    return render(
        request,
        "blog/blog_post.html",
        {"post": post_obj},
    )
