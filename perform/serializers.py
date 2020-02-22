from rest_framework.serializers import ModelSerializer
from .models import PerformPost


class PerformPostSerializer(ModelSerializer):
    class Meta:
        model = PerformPost
        read_only_fields = ('ip', 'author', 'created', 'updated')
        fields = ('text', ) + read_only_fields

