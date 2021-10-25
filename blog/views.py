from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# def home(request):
#     post = {'posts': Post.objects.all().order_by('-date_posted')}
#     return render(request, 'blog/home.html', post)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', {'title': 'Sobre'})
