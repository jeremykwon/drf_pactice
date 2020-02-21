from rest_framework.routers import DefaultRouter
from .views import (PostViewSet, UserReadOnlyViewSet,
                    ContentPostListAPIView,
                    ContentPostDetailAPIView, post_detail,
                    PostListAPIView, PostDetailAPIView,
                    PostListGenericsView, PostDetailGenericsView)
from django.urls import path, include

router = DefaultRouter()
router.register('viewset/post', PostViewSet)
router.register('viewset/readonly/user', UserReadOnlyViewSet)

urlpatterns = [
    path('', include(router.urls)),  # viewset 은 자동적으로 마지막에 / 가 붙는다
    # APIView(CBV)
    path('apiview/content/', ContentPostListAPIView.as_view()),
    path('apiview/content/<int:pk>/', ContentPostDetailAPIView.as_view()),
    # APIView(FBV)
    path('fbv/apiview/content/<int:pk>/', post_detail),  # 함수기반 뷰
    # mixin
    path('mixin/content/', PostListAPIView.as_view()),
    path('mixin/content/<int:pk>/', PostDetailAPIView.as_view()),
    # generics
    path('generics/content/', PostListGenericsView.as_view()),
    path('generics/content/<int:pk>/', PostDetailGenericsView.as_view()),

]
