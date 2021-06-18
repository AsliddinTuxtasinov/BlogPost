from django.urls import path
from main.views import index, postSlug, catagorySlug, search

urlpatterns = [
    path('', index, name="index"),
    path('search/',search,name="search_post"),
    path('catagory/<str:slug>', catagorySlug, name="catagory"),
    path('post/<slug:slug>', postSlug, name="post"),


]
