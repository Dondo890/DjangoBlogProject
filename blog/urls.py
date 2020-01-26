from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path('home/', PostListView.as_view(), name='homepage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new', PostCreateView.as_view(), name='post-new'),
]
