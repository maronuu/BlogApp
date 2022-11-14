from rest_framework import serializers

from .models import Category, Post, User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class LikedUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    liked_users = LikedUsersSerializer(many=True)
    
    class Meta:
        model = Post
        fields = "__all__"