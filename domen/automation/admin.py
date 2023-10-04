from django.contrib import admin, messages
from .models import Automation, Category


class CssFilter(admin.SimpleListFilter):
    title = 'Статус ра'
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
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title',)
    ordering = ['time_create', 'title']
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'cat__name']
    list_filter = [CssFilter, 'cat__name', 'is_published']

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, automation: Automation):
        return f"Описание {len(automation.content)} символов."

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
