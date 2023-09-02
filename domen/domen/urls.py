from django.contrib import admin
from django.urls import path
from automation.views import index, categories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('domen/', index),
    path('cat/', categories)
]
