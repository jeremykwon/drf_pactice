from django.conf import settings
from django.db import models


class TokenPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
