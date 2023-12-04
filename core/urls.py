from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.views import create_location
from core.views import (IndexView, GetDetailsJsonView,
                        LocationDetailsView, UpdateLocationView, DeleteLocationView)


app_name = 'index'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', IndexView.as_view(), name='category'),
    path('tinymce/', include('tinymce.urls')),
    path('<int:pk>', GetDetailsJsonView.as_view(), name='get_details_json'),
    path('location_details/<int:pk>/', LocationDetailsView.as_view(), name='location_details'),
    path('update_location/<int:pk>/', UpdateLocationView.as_view(), name='update_location'),
    path('create_location/<int:pk>/', create_location, name='create_location'),
    path('delete_location/<int:pk>/', DeleteLocationView.as_view(), name='delete_location'),


]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
