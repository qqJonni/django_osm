from django.contrib import admin

from likes.models import PlaceLikes


@admin.register(PlaceLikes)
class PlaceLikesAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['liked_by', 'place_post']
    list_display = ('place_post', 'place_post', 'like', 'created')


