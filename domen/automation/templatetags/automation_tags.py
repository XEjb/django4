from django import template
from django.db.models import Count

import automation.views as views
from automation.utils import menu
from ..models import Category, TagPost

register = template.Library()


@register.simple_tag
def get_menu():
    return menu


@register.inclusion_tag('automation/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('automation/list_tags.html')
def show_all_tags(cat_selected=0):
    return {'tags': TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)}
