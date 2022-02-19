from django.contrib import admin
from .models import Category, Article, Comment
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'article',)
    prepopulated_fields = {'slug': ('title',)} # new

admin.site.register(Article, ArticleAdmin)

admin.site.register(Category)
admin.site.register(Comment)