from django.shortcuts import render
from django.views import generic
from .models import Blog

# Create your views here.
def showBlogs(request):
    blogs = Blog.objects
    return render(request, 'blog/showblogs.html', {'blogs': blogs})
    