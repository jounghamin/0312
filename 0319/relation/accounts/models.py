from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bookmarks = models.ManyToManyField("articles.Article", related_name="bookmark_users")

    