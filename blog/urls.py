from django.urls import path
from .views import PostDetailView, PostListView, about


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', about, name='blog-about'),
]
