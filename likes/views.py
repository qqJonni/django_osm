from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import View

from users.models import User
from core.models import PlaceName, Comment
from likes.models import PlaceLikes, CommentLikes


class AddPlaceLikeView(View):
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


# def ajax_add_like_place(request):
#     place_post_id = int(request.POST.get('place_post_id'))
#     user_id = int(request.user.id)
#
#     data = {
#         'added': True,
#     }
#
#     user_inst = User.objects.get(id=user_id)
#     place_post_inst = PlaceName.objects.get(id=place_post_id)
#
#     try:
#         place_like_inst = PlaceLikes.objects.get(place_post=place_post_inst, liked_by=user_inst)
#     except Exception as e:
#         place_like = PlaceLikes(place_post=place_post_inst, liked_by=user_inst, like=True)
#         place_like.save()
#     return JsonResponse(data)


# def ajax_remove_like_place(request):
#     place_likes_id = int(request.POST.get('place_likes_id'))
#     user_id = int(request.user.id)
#     url_from = request.POST.get('url_from')
#
#     data = {
#         'removed': True,
#     }
#
#     place_like = PlaceLikes.objects.get(id=place_likes_id)
#     place_like.delete()
#
#     return JsonResponse(data)


class RemovePlaceLikeView(View):
    def post(self, request, *args, **kwargs):
        place_likes_id = int(request.POST.get('place_likes_id'))
        url_from = request.POST.get('url_from')

        place_like = PlaceLikes.objects.get(id=place_likes_id)
        place_like.delete()

        return redirect(url_from)


class AddCommentLikeView(View):
    def post(self, request, *args, **kwargs):
        comment_post_id = int(request.POST.get('comment_post_id'))
        print(comment_post_id)
        user_id = int(request.user.id)

        url_from = request.POST.get('url_from')

        user_inst = User.objects.get(id=user_id)
        comment_post_inst = Comment.objects.get(id=comment_post_id)

        try:
            comment_like_inst = CommentLikes.objects.get(comment_post=comment_post_inst, liked_by=user_inst)
        except Exception as e:
            comment_like = CommentLikes(comment_post=comment_post_inst, liked_by=user_inst, like=True)
            comment_like.save()
        return redirect(url_from)


class RemoveCommentLikeView(View):
    def post(self, request, *args, **kwargs):
        comment_likes_id_str = request.POST.get('comment_likes_id')
        if comment_likes_id_str is not None:
            comment_likes_id = int(comment_likes_id_str)
            url_from = request.POST.get('url_from')

            comment_like = CommentLikes.objects.get(id=comment_likes_id)
            comment_like.delete()

            return redirect(url_from)
        else:
            # Handle the case where comment_likes_id is None (optional)
            # You can log a message or return an error response
            pass
