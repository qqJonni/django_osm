from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View

from core.forms import PlaceForm, PlaceImageForm
from core.models import PlaceName, PlaceCategory, PlaceImage


class IndexView(ListView):
    model = PlaceName
    template_name = 'core/index.html'
    context_object_name = 'locations'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id:
            category = get_object_or_404(PlaceCategory, id=category_id)
            return PlaceName.objects.filter(category=category)
        return PlaceName.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['places_posts'] = {
            "type": "FeatureCollection",
            "features": [self.serialize_post(location) for location in context['locations']]
        }
        context['categories'] = PlaceCategory.objects.all()
        context['title'] = 'Where to Travel'
        return context

    def serialize_post(self, location):
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
                "image_urls": image_urls
            }
        }


class GetDetailsJsonView(View):
    def get(self, request, pk):
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


class LocationDetailsView(DetailView):
    model = PlaceName
    template_name = 'core/location_details.html'
    context_object_name = 'location'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pictures'] = self.object.pictures.all()
        context['list_locations'] = PlaceName.objects.all()
        return context


def create_location(request, pk):
    location = get_object_or_404(PlaceName.objects.prefetch_related('pictures'), pk=pk)

    if request.method == 'POST':
        form = PlaceForm(request.POST)
        image_form = PlaceImageForm(request.POST, request.FILES)

        if form.is_valid() and image_form.is_valid():
            new_location = form.save(commit=False)
            new_location.author = request.user
            new_location.save()
            picture = image_form.cleaned_data['picture']
            if picture:
                PlaceImage.objects.create(place=new_location, picture=picture)
            form.save_m2m()
            return redirect('index:index')
    else:
        form = PlaceForm()
        image_form = PlaceImageForm()

    context = {
        'location': location,
        'pictures': location.pictures.all(),
        'title': 'Location',
        'form': form,
        'image_form': image_form,
    }

    return render(request, 'core/create_location.html', context)




class UpdateLocationView(UpdateView):
    model = PlaceName
    form_class = PlaceForm
    template_name = 'core/update_location.html'
    context_object_name = 'location'

    def get_success_url(self):
        return reverse('index:location_details', args=[self.object.pk])


class DeleteLocationView(DeleteView):
    model = PlaceName
    template_name = 'core/delete_location.html'
    context_object_name = 'location'

    def get_success_url(self):
        return reverse('index:index')
# def serialize_post(location):
#     redirect_url = reverse('index:get_details_json', args=[location.pk])
#
#     image_urls = [image.show_photo_preview for image in location.pictures.all()]
#
#     return {
#         "type": "Feature",
#         "geometry": {
#             "type": "Point",
#             "coordinates": [location.longitude, location.latitude]
#         },
#         "properties": {
#             "title": location.title,
#             "detailsUrl": redirect_url,
#             "description_short": location.short_description,
#             "description_long": location.long_description,
#             "image_urls": image_urls
#         }
#     }
#
#
# def index(request, category_id=None):
#     if category_id:
#         category = PlaceCategory.objects.get(id=category_id)
#         locations = PlaceName.objects.filter(category=category)
#     else:
#         locations = PlaceName.objects.all()
#
#     context = {
#         'places_posts': {"type": "FeatureCollection",
#                          "features": [
#                              serialize_post(location) for location in locations
#                          ]}, 'locations': locations, 'categories': PlaceCategory.objects.all(),
#         'title': 'Where to Travel'
#     }
#     return render(request, 'core/index.html', context)
#
#
# def get_details_json(request, pk):
#     location = get_object_or_404(PlaceName.objects.prefetch_related('pictures'), pk=pk)
#
#     location_serialize = {
#         "title": location.title,
#         "imgs": [pic.picture.url for pic in location.pictures.order_by('sequence_number')],
#         "description_short": location.short_description,
#         "description_long": location.long_description,
#         "coordinates": {
#             "lng": location.longitude,
#             "lat": location.latitude
#         }
#     }
#
#     return JsonResponse(location_serialize, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})


# def location_details(request, pk):
#     location = get_object_or_404(PlaceName.objects.prefetch_related('pictures'), pk=pk)
#     locations = PlaceName.objects.all()
#
#     context = {
#         'location': location,
#         'pictures': location.pictures.all(),
#         'title': 'Location',
#         'list_locations': locations
#     }
#     return render(request, 'core/location_details.html', context)
#
#
# def create_location(request, pk):
#     location = get_object_or_404(PlaceName.objects.prefetch_related('pictures'), pk=pk)
#
#     if request.method == 'POST':
#         form = PlaceForm(request.POST)
#         image_form = PlaceImageForm(request.POST, request.FILES)
#
#         if form.is_valid() and image_form.is_valid():
#             new_location = form.save(commit=False)
#             new_location.author = request.user
#             new_location.save()
#             picture = image_form.cleaned_data['picture']
#             if picture:
#                 PlaceImage.objects.create(place=new_location, picture=picture)
#             form.save_m2m()
#             return redirect('index:index')
#     else:
#         form = PlaceForm()
#         image_form = PlaceImageForm()
#
#     context = {
#         'location': location,
#         'pictures': location.pictures.all(),
#         'title': 'Location',
#         'form': form,
#         'image_form': image_form,
#     }
#
#     return render(request, 'core/create_location.html', context)
#
#
# def update_location(request, pk):
#     location = PlaceName.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = PlaceForm(data=request.POST, instance=location)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('index:location_details', args=[pk]))
#     else:
#         form = PlaceForm(instance=location)
#     context = {
#         'form': form,
#         'location': location
#     }
#     return render(request, 'core/update_location.html', context)
#
#
# def delete_location(request, pk):
#     location = get_object_or_404(PlaceName, pk=pk)
#
#     if request.method == 'POST':
#         location.delete()
#         return redirect('index:index')
#
#     context = {
#         'location': location,
#     }
#     return render(request, 'core/delete_location.html', context)
