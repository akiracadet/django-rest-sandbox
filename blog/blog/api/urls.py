from django.urls import include
from django.urls import path


urlpatterns = [
    path('posts/', include('posts.urls')),
]
