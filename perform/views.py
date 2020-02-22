from rest_framework.viewsets import ModelViewSet
from .serializers import PerformPostSerializer
from .models import PerformPost

from rest_framework.permissions import AllowAny, IsAuthenticated

from .permissions import CustomIsAuthorOrReadonly


class PerformPostViewSet(ModelViewSet):
    queryset = PerformPost.objects.all()
    serializer_class = PerformPostSerializer

    # 인증된 유저에게만 권한을 부여한다.
    # 기본제공은 아래와 같다.
    # 1.AllowAny : 누구나
    # 2.IsAuthenticated : 인증된 요청에 한해서
    # 3.IsAdminUser : admin 유저인 경우만
    # 4.IsAuthenticatedOrReadOnly : 비인증 요청에게는 읽기 권한만 부여
    permission_classes = [CustomIsAuthorOrReadonly]

    # 유저의 ip 정보를 얻는 커스텀 함수인데 별로 필요없는 듯
    # 그냥 self.request.META.get('REMOTE_ADDR')로 하면 될듯
    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        print(ip)
        return ip

    # 현재 유저와 IP 주소를 저장
    # serializer.save()를 호출하면 validation 된 데이터들과
    # 지정해준 **kwargs 값들이 합쳐져서 저장된다.
    def perform_create(self, serializer):
        serializer.save(ip=self.get_client_ip(), author=self.request.user)
