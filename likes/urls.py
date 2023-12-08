from django.urls import path

from likes.views import AddCommentLikeView, RemoveCommentLikeView, AddPlaceLikeView, RemovePlaceLikeView

app_name = 'likes'

urlpatterns = [
    path('add/', AddPlaceLikeView.as_view(), name='add'),
    path('remove/', RemovePlaceLikeView.as_view(), name='remove'),

    path('add-comment/', AddCommentLikeView.as_view(), name='add-comment'),
    path('remove-comment/', RemoveCommentLikeView.as_view(), name='remove-comment'),

]
