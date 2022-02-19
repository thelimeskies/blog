from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.urls import reverse
from tinymce.models import HTMLField

Status = {
    0 : "Draft",
    1 : "Published",
    2 : "Reviewing"}

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumb_image = models.ImageField(upload_to = 'thumbs/')
    thumb_image2x = models.ImageField(upload_to = 'thumbs2x/')
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=False, unique=True)
    category = models.ManyToManyField(Category)
    tag = TaggableManager()
    article = HTMLField()
    featured = models.BooleanField(default=False)
    created_on = models.DateField(auto_now=True)
    summary = models.TextField()    
    
    def get_absolute_url(self):
        return reverse('article_details', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
class Comment(models.Model):
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateField()
    parent = models.ForeignKey("self", blank= True, null= True, related_name="+", on_delete=models.CASCADE)
    
    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_on')
    
    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False