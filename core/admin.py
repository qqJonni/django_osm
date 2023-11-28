from django.contrib import admin
from core.models import EVChargingLocation


@admin.register(EVChargingLocation)
class EvChargingLocationAdmin(admin.ModelAdmin):
    list_display = ['station_name', 'latitude', 'longitude']
