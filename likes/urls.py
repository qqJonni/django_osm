from django.urls import path, include

from likes.views import AddPlaceLikeView, RemovePlaceLikeView, AddCommentLikeView, RemoveCommentLikeView

app_name = 'likes'

urlpatterns = [
    path('likes/', include([
        path('add/', AddPlaceLikeView.as_view(), name='add'),
        path('remove/', RemovePlaceLikeView.as_view(), name='remove'),

        path('add-comment/', AddCommentLikeView.as_view(), name='add'),
        path('remove-comment/', RemoveCommentLikeView.as_view(), name='remove'),
    ]))
]
