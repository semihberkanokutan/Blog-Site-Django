from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blog/index.html', {
        "posts": latest_posts
    })


def all_blog_posts(request):
    return render(request, 'blog/all-posts.html')


def blog_post_detail(request):
    return render(request, 'blog/post-details.html')