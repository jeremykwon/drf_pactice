from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError  # 이외에도 여러 에러 발생이 정의되어 있다.
from first.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    # 모델 단에서 정의해주는 것이 맞지만 해당
    # 시리얼라이저 에서만 적용하고 싶은 경우 사용
    # text 필드에 대해서만 validate (정해진 형식이다)
    # 가급적이면 이 방법을 사용
    def validate_text(self, text):
        if '권' not in text:
            raise ValidationError('권 이 포함되어 있지 않습니다.')
        return text

    # 모든 필드에 대해서 validate (정해진 형식이다)
    def validate(self, data):
        if len(data['text']) < 2:
            raise ValidationError('글자의 길이는 2자 이상이되어야 합니다.')
        return data
