from django.urls import path
from .views import BlogPost, BlogView

urlpatterns = [
    path('', BlogView, name= 'blog'),
    path('<int:postid>', BlogPost, name= 'blog_post'),
]
