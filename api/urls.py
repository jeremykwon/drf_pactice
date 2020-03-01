from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TokenPostViewSet

router = DefaultRouter()
router.register('token_post', TokenPostViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
