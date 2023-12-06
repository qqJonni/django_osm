from django import template

from likes.models import CommentLikes


register = template.Library()

@register.simple_tag(takes_context=True)
def is_liked(context, comment_post_id):
    request = context['request']
    try:
        comment_likes = CommentLikes.objects.get(comment_post_id=comment_post_id, liked_by=request.user.id).like
    except Exception as e:
        comment_likes = False
    return comment_likes


@register.simple_tag()
def count_likes(comment_post_id):
    return CommentLikes.objects.filter(comment_post_id=comment_post_id, like=True).count()


@register.simple_tag(takes_context=True)
def comment_likes_id(context, comment_post_id):
    request = context['request']
    return CommentLikes.objects.get(comment_post_id=comment_post_id, liked_by=request.user.id).id
