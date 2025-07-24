# stylists/urls.py

from rest_framework.routers import DefaultRouter
from .views import StylistViewSet

router = DefaultRouter()
router.register(r'stylists', StylistViewSet, basename='stylist')

urlpatterns = router.urls
