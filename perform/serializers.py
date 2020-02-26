from rest_framework.serializers import (ModelSerializer, ReadOnlyField,
                                        CharField, SerializerMethodField)
from .models import PerformPost


class PerformPostSerializer(ModelSerializer):
    # 필드 임의 정의
    author_username = ReadOnlyField(source='author.username')
    maple = CharField(allow_blank=True, max_length=100, source='text')

    # 특정 필드 값 변경해서 사용하기
    test = SerializerMethodField(read_only=True)

    def get_test(self, obj):
        return obj.text + obj.text

    class Meta:
        model = PerformPost
        read_only_fields = ('ip', 'created', 'updated', 'maple', 'test')
        fields = ('text', 'author_username') + read_only_fields
