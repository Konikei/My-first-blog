from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    print("post_detail view function called with pk =", pk)
    # Retrieve the post object with the given primary key (pk)
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello, world!')


