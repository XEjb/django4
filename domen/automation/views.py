from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

data_db = [
    {'id': 1, 'title': 'Первый', 'content': 'Биография 1', 'is_published': True},
    {'id': 2, 'title': 'Второй', 'content': 'Биография 2', 'is_published': False},
    {'id': 3, 'title': 'Третий', 'content': 'Биография 3', 'is_published': True},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'automation/index.html', context=data)


def about(request):
    return render(request, 'automation/about.html', {'title': 'О сайте'})


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music',))
        return HttpResponseRedirect(uri)

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена 404</h1>')
