from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.views import get_details_json, index, location_details

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', index, name='category'),
    path('tinymce/', include('tinymce.urls')),
    path('<int:pk>', get_details_json, name='get_details_json'),
    path('location/<int:pk>/', location_details, name='location_details'),

]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
