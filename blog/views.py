from django.shortcuts import render

posts = [
    {
        'title': 'Post 1',
        'author': 'Pedro Achcar',
        'content': 'Primeiro post do blog!',
        'date_posted': '21/10/2021'
    },
    {
        'title': 'Post 2',
        'author': 'Pedro Lucas',
        'content': 'Segundo post do blog!',
        'date_posted': '20/10/2021'
    },
    {
        'title': 'Post 3',
        'author': 'Nathalia Costa',
        'content': 'Terceiro post do blog!',
        'date_posted': '22/10/2021'
    },
    {
        'title': 'Post 4',
        'author': 'Teste',
        'content': 'Quarto e último post o blog!',
        'date_posted': '23/10/2021'
    }
]


def home(request):
    post = {'posts': posts}
    return render(request, 'blog/home.html', post)


def about(request):
    return render(request, 'blog/about.html', {'title': ''})
