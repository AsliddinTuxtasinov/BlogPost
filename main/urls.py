from django.urls import path
from .views import Homepage, PostDetial, HompageViaCategoryView


urlpatterns = [
    path('', Homepage.as_view(), name="index"),
    path('category/<slug:slug>', HompageViaCategoryView.as_view(), name="category"),
    path('post/<slug:slug>', PostDetial.as_view(), name="post-detail"),
]
