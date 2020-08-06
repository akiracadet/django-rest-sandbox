from django.urls import path
from posts.views import PostListCreateAPIView
from posts.views import PostRetrieveUpdateAPIView
from posts.views import PostRetrieveDestroyAPIView


urlpatterns = [
    path('', PostListCreateAPIView.as_view()),
    path('<int:pk>/', PostRetrieveUpdateAPIView.as_view()),
    path('<int:pk>/delete/', PostRetrieveDestroyAPIView.as_view()),
]
