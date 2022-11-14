from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from .models import Comment, Post
from .serializers import PostSerializer


# =============↓サンプルコード================
def say_hello(request):
    return HttpResponse("Hello World")

# http://localhost:4989/blog/hoge/afsadas/?name=huga みたいな感じでアクセス


def display_title(request, title):
    request_path = request.path
    if "name" in request.GET:
        query_param_name = request.GET.get("name")
        print(query_param_name, "aaaaaaaa")
        return HttpResponse(f'タイトルは{title}です、クエリパラメーターnameは{query_param_name}です')
    return HttpResponse(f'タイトルは{title}です。')
# =============↑サンプルコード================


def post_list(request):
    out_text = ""
    posts = Post.objects.all()
    for post in posts:
        out_text += f"ID: {post.id} | Title: {post.title} | Body: {post.body} | CreatedAt: {post.created_at} | UpdatedAt: {post.updated_at} <br/>"
    return HttpResponse(out_text)

# Modelはmodels.py
# Vがビューでurls.py
# Cがコントローラーでviews.py

def post_detail_raw_django(request, post_id: int):
    this_post = get_object_or_404(Post, id=post_id)
    out_text = f"Title: {this_post.title} | Body: {this_post.body} | Category: {this_post.category.name}<br/>"


    comments = this_post.comments.all() # comments = Comment.objects.filter(post=this_post) でもOK!
    liked_users = this_post.liked_users.all()

    for comment in comments:
        out_text += f"Comment {comment.id}: From {comment.author} | {comment.content}<br/>"
    
    print(liked_users)
    out_text += "Liked by:"
    for liked_user in liked_users:
        out_text += f" {liked_user.username} "
    return HttpResponse(out_text)


def post_detail(reqeust, post_id):
    this_post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(this_post)
    return JsonResponse(serializer.data)