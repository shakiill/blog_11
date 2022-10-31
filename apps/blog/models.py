from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_blog')
    thumbnail = models.ImageField(upload_to='blog')
    short_description = models.TextField()
    description = models.TextField()
    tag = models.ManyToManyField(Tag, blank=True, related_name='tag_blog')
    author = models.ForeignKey(User, on_delete=SET_NULL, null=True, blank=True, related_name='author_blog')
    created_at = models.DateField(auto_now_add=True)
    edited_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
