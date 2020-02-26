from first.models import Post
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .pagination import PostPagination

from rest_framework.filters import SearchFilter

# from rest_framework.throttling import UserRateThrottle

from .throttles import UserCustomRateThrottle


# filter, pagination
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    pagination_class = PostPagination  # 페이지네이션 클래스 커스텀 정의

    # ?search 로써 (search 인자를 포함하여 요청시) 검색이 가능하다
    filter_backends = [SearchFilter]
    search_fields = ['text', 'id']  # id, text 를 검색 가능하도록.

    # 각 뷰별로 접근 제한을 지정 하는 방법(1)
    # throttle_classes = UserRateThrottle
    # 각 뷰별로 접근 제한을 지정하는 방법(2) -> 코드가 조금더 간단해진다.
    # setting.py에 지정되어 있다.
    throttle_scope = 'custom'
    # 각 유저별로 접근 제한
    # (커스텀) 현재는 profile 과 is_premium 을 구현하지 않아 사용 불가
    # throttle_classes = [UserCustomRateThrottle]



    '''
    def get_queryset(self):
        qs = super().get_queryset()  # 정의한 쿼리셋 획득
        # 자신의 글만 보여줌
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()  # 비어있다.
        return qs
    '''
