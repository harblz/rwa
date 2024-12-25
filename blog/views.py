from django.shortcuts import render

from .models import Post

def index(request):
    posts = Post.objects.filter(status="p").order_by("-published_date")
    return render(request, "index.html", { 'posts': posts })