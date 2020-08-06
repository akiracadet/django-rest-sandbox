from rest_framework import generics
from rest_framework import permissions
from posts.permissions import IsAuthor
from posts.serializers import PostSerializer
from posts.models import Post


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthor, )

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDestroyAPIView(generics.DestroyAPIView):
    permission_classes = (IsAuthor, )

    queryset = Post.objects.all()
    serializer_class = PostSerializer
