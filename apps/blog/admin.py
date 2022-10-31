from django.contrib import admin

from apps.blog.models import Blog, Tag, Category

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Blog)
