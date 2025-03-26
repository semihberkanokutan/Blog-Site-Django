from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main-page"),
    path('posts/', views.all_blog_posts, name='all-posts-page'),
    path('posts/post', views.blog_post_detail)
]
