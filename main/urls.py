from django.urls import path
from .views.blog_view import IndexView, CategoryView, DetailView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='HomePage'),
    path('<slug:slug>', DetailView.as_view(), name='article_details'),
    path("categories/", CategoryView.as_view(), name="category"),
    path("about/", AboutView.as_view(), name="about")
]
