from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.views import get_details_json, index, location_details, create_location, update_location, delete_location

app_name = 'index'

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', index, name='category'),
    path('tinymce/', include('tinymce.urls')),
    path('<int:pk>', get_details_json, name='get_details_json'),
    path('location_details/<int:pk>/', location_details, name='location_details'),
    path('update_location/<int:pk>/', update_location, name='update_location'),
    path('create_location/<int:pk>/', create_location, name='create_location'),
    path('delete_location/<int:pk>/', delete_location, name='delete_location'),


]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
