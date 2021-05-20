from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm, PostForm
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    blogs = Blog.objects.filter(status='published')
    categories = Category.objects.all()
    template_name = 'blog/index.html'
    context = {'blogs': blogs, 'categories': categories}
    return render(request, template_name, context)

def detail_view(request, id):
    blog = get_object_or_404(Blog, id=id)
    template_name = 'blog/detail_view.html'
    context = {'blog': blog}
    return render(request, template_name, context)

def category_view(request, cat):
    post_categories = Blog.objects.filter(category=cat)
    template_name = 'blog/categories.html'
    context = {'posts': post_categories}
    return render(request, template_name, context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
           
        else:
            return render(request, 'blog/login.html', {'message': 'login failed, please try again'})
    else:
        return render(request, 'blog/login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_signup(request):
    form = NewUserForm
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, "Registration successful." )
            return redirect("user_login")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            form = NewUserForm
	
    template_name = 'blog/register.html'
    context = {"form": form}
    return render(request, template_name, context)

def base_template(request):
    cat_options = Category.objects.all()
    template_name = 'blog/base.html'
    context = {'categories': cat_options}
    return render(request, template_name, context)

def add_blog(request):
    post = Blog.objects.all()
    cats = Category.objects.all()
    form = PostForm()
    message = ""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, 'Registration Successful')
            return redirect('index')

    else:
        
        message = "error in forms... please try again"
        form = PostForm()

    context = {'form': form, 'message': message, 'posts': post, 'categories': cats}
    return render(request, 'blog/add_blog.html', context)

    # template_name = 'blog/add_blog.html'
    # context = {}
    # return render(request, template_name, context)