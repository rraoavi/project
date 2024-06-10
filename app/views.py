from django.shortcuts import render
from django.conf import settings
from urllib import request
from django.http import HttpResponse,HttpResponseRedirect
from .models import Blog
from django .shortcuts import get_object_or_404
#from django.views import View


# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    print(blogs, 'blogs')
    return render(request,"app/home.html", {'blogs': blogs})

def skills(request):
    return render(request,"app/home.html")
def connect(request):
    return render(request,"app/home.html")
# def blog(request):
#     return render(request,"app/home.html")

def all_blogs(request):
    blogs = Blog.objects.all()
    print(blogs, 'blogs')
    return render(request, 'app/home.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'app/blog_detail.html', {'blog': blog})
