from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_category": ("category",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_post": ("title",)}
