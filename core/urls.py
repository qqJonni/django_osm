from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from core.views import get_details_json, index

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', index, name='category'),
    path('tinymce/', include('tinymce.urls')),
    path('<int:pk>', get_details_json, name='get_details_json'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
