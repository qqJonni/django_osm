from django.shortcuts import redirect
from django.views.generic import View

from users.models import User
from core.models import PlaceName
from likes.models import PlaceLikes


class AddLikeView(View):
    def post(self, request, *args, **kwargs):
        place_post_id = int(request.POST.get('place_post_id'))
        user_id = int(request.user.id)

        url_from = request.POST.get('url_from')

        user_inst = User.objects.get(id=user_id)
        place_post_inst = PlaceName.objects.get(id=place_post_id)

        try:
            place_like_inst = PlaceLikes.objects.get(place_post=place_post_inst, liked_by=user_inst)
        except Exception as e:
            place_like = PlaceLikes(place_post=place_post_inst, liked_by=user_inst, like=True)
            place_like.save()
        return redirect(url_from)


class RemoveLikeView(View):
    def post(self, request, *args, **kwargs):
        place_likes_id = int(request.POST.get('place_likes_id'))
        url_from = request.POST.get('url_from')

        place_like = PlaceLikes.objects.get(id=place_likes_id)
        place_like.delete()

        return redirect(url_from)


