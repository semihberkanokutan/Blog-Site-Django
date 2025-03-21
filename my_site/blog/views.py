from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def all_blog_posts(request):
    return HttpResponse('All Blog Posts')