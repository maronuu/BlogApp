from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "blog"

urlpatterns = [
    # /blog: blog list
    path("", views.PostList.as_view(), name="post_list"),
    # /blog/1(int): blog detail
    path("<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
