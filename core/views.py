from django.db.models import Count
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from core.forms import PlaceForm, PlaceImageForm, CommentForm
from core.models import PlaceName, PlaceCategory, PlaceImage
from likes.models import PlaceLikes

"""Эта переменная отвечает за отображение постов на главной странице с минимальным колличеством лайков указанных в переменной"""
_LIKE = 2


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
        queryset = PlaceName.objects.all()
        context['likes'] = queryset.annotate(like_count=Count('placelikes')).filter(like_count__gte=_LIKE).order_by('-like_count')
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
                "image_urls": image_urls,
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


class LocationDetailsView(FormMixin, DetailView):
    model = PlaceName
    template_name = 'core/location_details.html'
    context_object_name = 'location'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('index:location_details', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.place = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pictures'] = self.object.pictures.all()
        context['list_locations'] = PlaceName.objects.filter(author=self.object.author).exclude(pk=self.object.pk)
        return context


def create_location(request, pk):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        image_form = PlaceImageForm(request.POST, request.FILES)  # Обработка изображений

        if form.is_valid() and image_form.is_valid():
            new_location = form.save(commit=False)
            new_location.author = request.user
            new_location.save()

            # Обработка изображений
            for picture in request.FILES.getlist('picture'):
                PlaceImage.objects.create(place=new_location, picture=picture)

            return redirect('index:index')
    else:
        form = PlaceForm()
        image_form = PlaceImageForm()

    context = {
        'title': 'Location',
        'form': form,
        'image_form': image_form,
        'pk': pk
    }

    return render(request, 'core/create_location.html', context)


def update_location(request, pk):
    location = PlaceName.objects.get(pk=pk)
    if request.method == 'POST':
        form = PlaceForm(data=request.POST, instance=location)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index:location_details', args=[pk]))
    else:
        form = PlaceForm(instance=location)
    context = {
        'form': form,
        'location': location
    }
    return render(request, 'core/update_location.html', context)


class DeleteLocationView(LoginRequiredMixin, DeleteView):
    model = PlaceName
    template_name = 'core/delete_location.html'
    context_object_name = 'location'

    def get_success_url(self):
        return reverse('index:index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
