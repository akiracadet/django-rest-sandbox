from django.urls import path
from api.views import BookListAPIView


urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
]
