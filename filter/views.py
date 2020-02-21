from first.models import Post
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer

from rest_framework.filters import SearchFilter


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # ?search 로써 (search 인자를 포함하여 요청시) 검색이 가능하다
    filter_backends = [SearchFilter]
    search_fields = ['text', 'id']  # id, text 를 검색 가능하도록.

    def get_queryset(self):
        qs = super().get_queryset()  # 정의한 쿼리셋 획득
        # 자신의 글만 보여줌
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()  # 비어있다.
        return qs
