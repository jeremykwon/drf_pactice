from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import TokenPost
from rest_framework.viewsets import ModelViewSet
from .serializers import TokenPostSerializer

from django.conf import settings
from django.db.models.signals import post_save  # db save (create)이벤트시 실행되도록
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# 토큰 생성 방법 (2)
# 유저 모델 생성시 실행되는 함수
# token 값을 만든다.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class CustomTokenAuthentication(TokenAuthentication):
    keyword = 'custom_auth'


class TokenPostViewSet(ModelViewSet):
    queryset = TokenPost.objects.all()
    serializer_class = TokenPostSerializer
    
    # 인증 클래스를 토큰인증으로( 기본 )
    # TokenAuthentication 을 상속받아 keyword 값을 변경해준다. ( 기본값 Token )
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    # create 재정의
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
