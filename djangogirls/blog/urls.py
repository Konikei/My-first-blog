from django.urls import path
from . import views
from django.shortcuts import render
from .models import Post


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='postdetail'),
    path('hello/', views.hello, name='hello'),
    path('post/new/', views.post_new, name='post_new'),
]

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def post_detail(request, pk):
    # Retrieve the post object with the given primary key (pk)
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

