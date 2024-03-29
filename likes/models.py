from django.db import models

from django.conf import settings
from django.utils import timezone

from core.models import PlaceName, Comment


class PlaceLikes(models.Model):
    place_post = models.ForeignKey(PlaceName, on_delete=models.SET_NULL, null=True, verbose_name='Пост к месту')
    liked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Поставил лайк')
    like = models.BooleanField('Like', default=False)
    created = models.DateTimeField('Дата и время', default=timezone.now)

    def __str__(self):
        return f'{self.liked_by}: {self.place_post}-{self.like}'

    class Meta:
        verbose_name = 'Place like'
        verbose_name_plural = 'Place likes'


class CommentLikes(models.Model):
    comment_post = models.ForeignKey(Comment, on_delete=models.SET_NULL, null=True, verbose_name='Комментарий к посту')
    liked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='Поставил лайк')
    like = models.BooleanField('Like', default=False)
    created = models.DateTimeField('Дата и время', default=timezone.now)

    def __str__(self):
        return f'{self.liked_by}: {self.comment_post}-{self.like}'

    class Meta:
        verbose_name = 'Comment like'
        verbose_name_plural = 'Comment likes'
