from django import template

from likes.models import PlaceLikes


register = template.Library()

@register.simple_tag(takes_context=True)
def is_liked(context, place_post_id):
    request = context['request']
    try:
        place_likes = PlaceLikes.objects.get(place_post_id=place_post_id, liked_by=request.user.id).like
    except Exception as e:
        place_likes = False
    return place_likes


@register.simple_tag()
def count_likes(place_post_id):
    return PlaceLikes.objects.filter(place_post_id=place_post_id, like=True).count()


@register.simple_tag(takes_context=True)
def place_likes_id(context, place_post_id):
    request = context['request']
    return PlaceLikes.objects.get(place_post_id=place_post_id, liked_by=request.user.id).id
