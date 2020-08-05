from django.urls import path
from books.views import BookListAPIView
from books.views import BookDetailAPIView


urlpatterns = [
    path('', BookListAPIView.as_view()),
    path('<int:pk>/', BookDetailAPIView.as_view()),
]
