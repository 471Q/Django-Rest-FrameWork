from django.urls import path

from .views import InventoryViewSet
from rest_framework.routers import DefaultRouter

app_name = 'inventory_api'

router = DefaultRouter()
router.register('', InventoryViewSet, basename='inventory')
urlpatterns = router.urls
