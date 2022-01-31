from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Category, Post


class Homepage(View):
    def get(self, request):
        category = Category.objects.all()
        posts = Post.objects.all().order_by('-id')

        search_query = request.GET.get("q", "")
        if search_query:
            posts = Post.objects.filter(title__icontains=search_query).order_by('id')

        context = {
            "posts": posts,
            "category": category,
            "search_query": search_query
        }
        return render(request, "index.html", context)


class HompageViaCategoryView(View):
    def get(self, request, slug):
        cat = get_object_or_404(Category, slug_category=slug)
        posts = Post.objects.filter(category=cat).order_by('id')
        category = Category.objects.all()

        context = {
            "posts": posts,
            "category": category
        }
        return render(request, "index.html", context)


class PostDetial(View):
    def get(self, request, slug):
        category = Category.objects.all()
        post = get_object_or_404(Post, slug_post=slug)

        context = {
            "post": post,
            "category": category
        }
        return render(request, "post-detal.html", context)
