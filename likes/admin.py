from django.contrib import admin

from likes.models import PlaceLikes, CommentLikes


@admin.register(PlaceLikes)
class PlaceLikesAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['liked_by', 'place_post']
    list_display = ('place_post', 'place_post', 'like', 'created')


@admin.register(CommentLikes)
class CommentLikesAdmin(admin.ModelAdmin):
    list_display = ('comment_post', 'liked_by', 'like', 'created')
