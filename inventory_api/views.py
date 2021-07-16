from rest_framework import generics
from inventory_api.models import Inventory, Supplier
from .serializers import  InventorySerializer, SupplierSerializer, CustomInventorySerializer

class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = CustomInventorySerializer

class InventoryDetail(generics.ListAPIView):
    serializer_class = InventorySerializer

    def get_queryset(self):
        slug = self.request.query_params.get('name', None)
        return Inventory.objects.filter(name=slug)

class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierDetail(generics.RetrieveDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
