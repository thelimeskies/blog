from re import template
from django.views.generic import ListView, DetailView, TemplateView
from ..models import Article
"""class IndexView(TemplateView):
    template_name = 'index.html'"""
    
class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    paginate_by = 12
    
class DetailView(DetailView):
    template_name = 'details.html'
    model = Article    

class CategoryView(TemplateView):
    template_name = 'category.html'
    
class AboutView(TemplateView):
    template_name = "about.html"

