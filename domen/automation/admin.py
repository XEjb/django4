from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Automation, Category


class CssFilter(admin.SimpleListFilter):
    title = 'Статус s'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('prod', 'прод'),
            ('inf', 'инф'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'prod':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'inf':
            return queryset.filter(husband__isnull=True)


@admin.register(Automation)
class AutomationAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'husband', 'tags']
    # exclude = ['tags', 'is_published']
    readonly_fields = ['post_photo']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title',)
    ordering = ['time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'cat__name']
    list_filter = [CssFilter, 'cat__name', 'is_published']
    save_on_top = True

    @admin.display(description='Изображение', ordering='content')
    def post_photo(self, automation: Automation):
        if automation.photo:
            return mark_safe(f"<img src='{automation.photo.url}' width=50>")
        return 'Без фото'

    @admin.action(description='Опубликовать')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Automation.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Automation.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
