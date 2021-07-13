from django.urls import path

from .views import InventoryList, InventoryDetail, supplierList, supplierDetail

app_name = 'inventory_api'

urlpatterns = [
    path('inventory/', InventoryDetail.as_view(), name='detail'),
    path('inventory', InventoryList.as_view(), name='list'),
]