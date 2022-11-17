from django.contrib import admin

from .models import Category, Comment, Post

# Django管理サイトでPostモデルを管理できるようにする


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
