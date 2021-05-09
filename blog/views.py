from django.shortcuts import render, get_object_or_404
from .models import Blog

def index(request):
    blogs = Blog.objects.filter(status='published')
    template_name = 'blog/index.html'
    context = {'blogs': blogs}
    return render(request, template_name, context)

def detail_view(request, id):
    blog = get_object_or_404(Blog, id=id)
    template_name = 'blog/detail_view.html'
    context = {'blog': blog}
    return render(request, template_name, context)