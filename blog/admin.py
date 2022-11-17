from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Comment, Post


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
