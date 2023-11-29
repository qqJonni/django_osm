from django.shortcuts import render
from core.models import EVChargingLocation
import json


def index(request):
    stations = list(EVChargingLocation.objects.values('latitude', 'longitude', 'station_name')[:])
    stations_json = json.dumps(stations)  # Преобразование в формат JSON
    context = {'stations_json': stations_json}
    return render(request, 'index.html', context)
