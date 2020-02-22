from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerformPostViewSet

router = DefaultRouter()
router.register('', PerformPostViewSet)

urlpatterns = [
    path('/', include(router.urls)),
]
