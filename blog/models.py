from django.db import models
from django.contrib.auth.models import User

# postモデルを作成
# https://docs.google.com/spreadsheets/d/1AJ53UH7X1NMX8gIoEsnmCxK3_xw0u3rF3S7HAWz5ly4/edit?usp=sharing


# 1対多の関係


class Category(models.Model):
    # id
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL
    )  # on_deleteはCategoryが削除されたときの挙動

    # 多対多
    liked_users = models.ManyToManyField(User, related_name="liked_posts", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(
        Post, null=True, on_delete=models.CASCADE, related_name="comments"
    )

    def __str__(self):
        return self.content
