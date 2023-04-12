from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

def post_list(request):
    return render(request, 'blog/post_list.html', {})