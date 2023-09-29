from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

from .models import Automation

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
        ]

data_db = [
    {'id': 1, 'title': 'Первый', 'content': 'one', 'is_published': True},
    {'id': 2, 'title': 'Второй', 'content': 'two 2', 'is_published': False},
    {'id': 3, 'title': 'Третий', 'content': 'three', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'one'},
    {'id': 2, 'name': 'two'},
    {'id': 3, 'name': 'three'},
]


def index(request):
    posts = Automation.published.all()

    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }
    return render(request, 'automation/index.html', context=data)


def about(request):
    return render(request, 'automation/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_slug):
    post = get_object_or_404(Automation, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'posts': post,
        'cat_selected': 1,
    }

    return render(request, 'automation/post.html', data)


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'automation/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена 404</h1>')
