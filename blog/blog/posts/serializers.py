from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content')

    
    def create(self, validated_data):
        user = None
        post = None
        request = self.context.get('request')

        if request and hasattr(request, 'user'):
            user = request.user
            post = Post(author=user, title=validated_data['title'], content=validated_data['content'])
            post.save()

        return post
