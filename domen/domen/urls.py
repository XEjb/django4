from django.contrib import admin
from django.urls import path, include
from automation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('automation.urls')),
]
