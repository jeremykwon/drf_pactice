from rest_framework.serializers import ModelSerializer
from .models import Post, ContentPost
from django.contrib.auth import get_user_model


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class ContentPostSerializer(ModelSerializer):
    class Meta:
        model = ContentPost
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        read_only_fields = ('pk', 'username')
        fields = read_only_fields + ('email', 'is_superuser')
