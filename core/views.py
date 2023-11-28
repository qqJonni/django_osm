from django.shortcuts import render
from core.models import EVChargingLocation


def index(request):
    stations = list(EVChargingLocation.objects.values('latitude', 'longitude')[:])
    context = {'stations': stations}
    return render(request, 'index.html', context)
