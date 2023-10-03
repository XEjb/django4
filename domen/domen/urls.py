from django.contrib import admin
from django.urls import path, include
from automation import views
from automation.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('automation.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

handler404 = page_not_found


admin.site.site_header = 'Adminka'
admin.site.index_title = 'ix'
