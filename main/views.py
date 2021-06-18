from django.shortcuts import render
from main.models import Catagory, Post
from django.db.models import Q


def index(request):
    posts = Post.objects.all()
    catagory = Catagory.objects.all()

    template_name = "index.html"
    return render(request, template_name, {
        "posts":posts,
        "catagory":catagory
    })

def search(request):
    if 'search' in request.GET:
        q = request.GET['search']
        posts = Post.objects.filter(catagory__icontains = q)
    else:
        posts = Post.objects.all()

    catagory = Catagory.objects.all()
            
    template_name = "index.html"
    return render(request, template_name, {
        "posts":posts,
        "catagory":catagory
    })

def catagorySlug(request, slug):
    posts = Post.objects.filter(catagory=slug)
    print(posts)
    catagory = Catagory.objects.all()

    template_name = "index.html"
    return render(request,template_name, {
        "posts":posts,
        "catagory":catagory
    })

def postSlug(request, slug):
    post = Post.objects.get(slug_post=slug)
    catagory = Catagory.objects.all()

    template_name = "post-detal.html"
    return render(request,template_name, {
        "post":post,
        "catagory":catagory
    })