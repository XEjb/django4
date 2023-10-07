from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband


@deconstructible
class Validator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзиёклмнопрстуфхцчшщьыъэюя0123456789- "
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else 'Должны присутствовать только рус символы'

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=4, label='Заголовок',
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            # validators=[
                            #     Validator(),
                            # ],
                            error_messages={
                                'min_length': 'Короткий заголовок'
                            })
    slug = forms.SlugField(max_length=255, label='URL',
                           validators=[
                               MinLengthValidator(5, message='Минимум 5 символов'),
                               MaxLengthValidator(100),
                           ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label='Content')
    is_published = forms.BooleanField(required=False, initial=True, label='status')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана', label='Категории')
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label='husband')

    def clean_title(self):
        title = self.clean_title['title']
        ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзиёклмнопрстуфхцчшщьыъэюя0123456789- "

        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError('Должны присутствовать только рус символы')