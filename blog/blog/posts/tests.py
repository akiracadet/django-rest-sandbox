from django.test import TestCase

from django.contrib.auth.models import User
from posts.models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="testuser", password="postmodeltestpassword")
        user.save()

        post = Post.objects.create(author=user, title="Post Title", content="Post Content")
        post.save()


    def test_post(self):
        user = User.objects.get(id=1)
        post = Post.objects.get(id=1)

        self.assertEquals(post.author, user)
        self.assertEquals(post.title, 'Post Title')
        self.assertEquals(post.content, 'Post Content')
