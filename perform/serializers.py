from rest_framework.serializers import ModelSerializer, ReadOnlyField, CharField
from .models import PerformPost


class PerformPostSerializer(ModelSerializer):
    # 필드 임의 정의
    author_username = ReadOnlyField(source='author.username')
    maple = CharField(allow_blank=True, max_length=100, source='text')

    class Meta:
        model = PerformPost
        read_only_fields = ('ip', 'created', 'updated', 'maple')
        fields = ('text', 'author_username') + read_only_fields

