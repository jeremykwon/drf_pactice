from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from .models import Post, ContentPost
from .serializers import PostSerializer, ContentPostSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.decorators import api_view

from rest_framework import mixins, generics


# ViewSet : List Retrieve Destroy Update Create
class UserViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


'''
# 원래대로라면 ViewSet 은  호출될 함수와 호출할 함수를 지정해준다
# router 를 통해 이러한 작업 생략 가능
user_list = UserViewSet.aS_view({
    'get' : 'list',
})
user_detail = UserViewSet.aS_view({
    'get' : 'retrieve',
})

## urls.py ##
path('user', user_list)
path('user/<int:pk>', user_detail)
'''


# ReadOnly ViewSet : List Retrieve
class UserReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# APIView List
class ContentPostListAPIView(APIView):
    # get 요청의 경우 Post 전체 list 를 보여줌
    def get(self, request):
        # model instance 인 경우 무관, 쿼리셋인경우 many=true
        serializer = ContentPostSerializer(ContentPost.objects.all(), many=True)
        return Response(serializer.data)

    # post 의 경우 받은 데이터를 통해 DB 저장
    def post(self, request):
        serializer = ContentPostSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.error, status=400)


# APIView Detail
class ContentPostDetailAPIView(APIView):
    def get(self, request, pk):
        content_post = get_object_or_404(ContentPost, pk=pk)
        serializer = ContentPostSerializer(content_post)
        return Response(serializer.data)

    def put(self, request, pk):
        content_post = get_object_or_404(ContentPost, pk=pk)
        serializer = ContentPostSerializer(content_post, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        content_post = get_object_or_404(ContentPost, pk=pk)
        content_post.delete()
        return Response(status=204)


# FBV 로써의 구현
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    content_post = get_object_or_404(ContentPost, pk=pk)

    if request.method == 'GET':
        serializer = ContentPostSerializer(content_post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContentPostSerializer(content_post, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    else:
        content_post.delete()
        return Response(status=204)


# mixin 사용 -> 여기서도 각 method 를 구분해야한다.
# 가변 인자 사용하지 않아도 괜찮다
class PostListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = ContentPost.objects.all()
    serializer_class = ContentPostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# mixin 사용 -> 여기서도 각 method 를 구분해야한다.
class PostDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = ContentPost.objects.all()
    serializer_class = ContentPostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.Update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Generic List, Create View
class PostListGenericsView(generics.ListCreateAPIView):
    queryset = ContentPost.objects.all()
    serializer_class = ContentPostSerializer


# Generic Retrieve, Update, Destroy View
class PostDetailGenericsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentPost.objects.all()
    serializer_class = ContentPostSerializer
