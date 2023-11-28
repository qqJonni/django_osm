import json
from django.conf import settings
from django.core.management.base import BaseCommand
from core.models import EVChargingLocation


class Command(BaseCommand):
    help = 'Load data from EV Station JSON file'

    def handle(self, *args, **kwargs):
        data_file = settings.BASE_DIR / 'data' / ' ski_resort.json'

        with open(data_file, 'r') as jsonfile:
            data = json.load(jsonfile)

        for record in data:
            # add the data to the database
            EVChargingLocation.objects.get_or_create(
                station_name=record['station_name'],
                latitude=record['latitude'],
                longitude=record['longitude']
            )
