from django.contrib import admin
from django.urls import path, include
from automation import views
from automation.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('automation.urls')),
]

handler404 = page_not_found
