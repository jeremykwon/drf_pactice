from django.db import models
from django.conf import settings


class PerformPost(models.Model):
    # 필수 필드이며 외래키 이므로 migrations 시 default 값을 지정해야 한다. ex) 1
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(null=True, blank=True)
    text = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
