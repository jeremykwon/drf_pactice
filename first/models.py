from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


# model validation 예시
def validate_text(value):
    if '욕' in value:
        raise ValidationError('금지된 말이 들어가 있습니다.')
    return value


class Post(models.Model):
    # 필수 필드이며 외래키 이므로 migrations 시 default 값을 지정해야 한다. ex) 1
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(validators=[validate_text])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)  # 역순 정렬


class ContentPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
