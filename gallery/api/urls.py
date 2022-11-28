from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GallaryViewSet

router = DefaultRouter()
router.register('gallery', GallaryViewSet, basename="gallery")

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
