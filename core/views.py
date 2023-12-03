from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from core.models import PlaceName, PlaceCategory


def serialize_post(location):
    redirect_url = reverse('index:get_details_json', args=[location.pk])

    image_urls = [image.show_photo_preview for image in location.pictures.all()]

    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [location.longitude, location.latitude]
        },
        "properties": {
            "title": location.title,
            "detailsUrl": redirect_url,
            "description_short": location.short_description,
            "description_long": location.long_description,
            "image_urls": image_urls[0]  # Pass the entire list of image URLs
        }
    }


def index(request, category_id=None):
    if category_id:
        category = PlaceCategory.objects.get(id=category_id)
        locations = PlaceName.objects.filter(category=category)
    else:
        locations = PlaceName.objects.all()

    context = {
        'places_posts': {"type": "FeatureCollection",
                         "features": [
                             serialize_post(location) for location in locations
                         ]}, 'locations': locations, 'categories': PlaceCategory.objects.all(),
        'title': 'Where to Travel'
    }
    return render(request, 'index.html', context)


def get_details_json(request, pk):
    location = get_object_or_404(PlaceName.objects.prefetch_related('pictures'), pk=pk)

    location_serialize = {
        "title": location.title,
        "imgs": [pic.picture.url for pic in location.pictures.order_by('sequence_number')],
        "description_short": location.short_description,
        "description_long": location.long_description,
        "coordinates": {
            "lng": location.longitude,
            "lat": location.latitude
        }
    }

    return JsonResponse(location_serialize, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})


def location_details(request, pk):
    location = get_object_or_404(PlaceName.objects.prefetch_related('pictures'), pk=pk)

    context = {
        'location': location,
        'pictures': location.pictures.all(),
        'title': 'Location'
    }
    return render(request, 'location_details.html', context)

