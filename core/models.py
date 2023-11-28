from django.db import models


class EVChargingLocation(models.Model):
    station_name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.station_name

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural ='Координаты'
