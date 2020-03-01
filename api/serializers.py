from rest_framework.serializers import ModelSerializer, ReadOnlyField

from api.models import TokenPost


class TokenPostSerializer(ModelSerializer):
    author_username = ReadOnlyField(source='author.username')

    class Meta:
        model = TokenPost
        fields = ('id', 'author_username', 'message', 'photo')
