from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    #path('hello', views.say_hello, name="hello"),
    # /blog/hoge/ここ可変(str) 
    #path('hoge/<str:title>/', views.display_title, name="display_title"),


    # /blogでブログ一覧
    path('', views.post_list, name="post_list"),
    # /blog/1(int)でブログ詳細
    path('<int:post_id>/', views.post_detail, name="post_detail"),
]
