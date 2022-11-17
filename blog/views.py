from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Comment, Post
from .serializers import PostSerializer


# ===Function based===
# def post_list(request):
#     out_text = ""
#     posts = Post.objects.all()
#     for post in posts:
#         out_text += f"ID: {post.id} | Title: {post.title} | Body: {post.body} | CreatedAt: {post.created_at} | UpdatedAt: {post.updated_at} <br/>"
#     return HttpResponse(out_text)


# def post_detail(reqeust, post_id):
#     this_post = get_object_or_404(Post, id=post_id)
#     serializer = PostSerializer(this_post)
#     return JsonResponse(serializer.data)


class PostList(APIView):
    """List all posts, or create a new post."""

    def get(self, request, format=None) -> Response:
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None) -> Response:
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """Get, update, delete a post instance"""

    def get(self, request: Request, pk: int, format=None) -> Response:
        post = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request: Request, pk: int, format=None) -> Response:
        post = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format=None) -> Response:
        post = get_object_or_404(Post, id=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Modelはmodels.py
# Vがビューでurls.py
# Cがコントローラーでviews.py

# def post_detail_raw_django(request, post_id: int):
#     this_post = get_object_or_404(Post, id=post_id)
#     out_text = f"Title: {this_post.title} | Body: {this_post.body} | Category: {this_post.category.name}<br/>"


#     comments = this_post.comments.all() # comments = Comment.objects.filter(post=this_post) でもOK!
#     liked_users = this_post.liked_users.all()

#     for comment in comments:
#         out_text += f"Comment {comment.id}: From {comment.author} | {comment.content}<br/>"

#     print(liked_users)
#     out_text += "Liked by:"
#     for liked_user in liked_users:
#         out_text += f" {liked_user.username} "
#     return HttpResponse(out_text)
