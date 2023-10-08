from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from domen import settings
from automation import views
from automation.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('automation.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found

admin.site.site_header = 'Adminka'
admin.site.index_title = 'ix'
