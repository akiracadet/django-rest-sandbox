from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    title = models.CharField(max_length=128, blank=False, null=False)
    content = models.TextField(blank=False, null=False)


    def __str__(self):
        return self.title
