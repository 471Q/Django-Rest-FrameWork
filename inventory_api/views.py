from rest_framework import generics
from inventory.models import Inventory, Supplier
from .serializers import  InventorySerializer, supplierSerializer, CustomInventorySerializer
# Create your views here.

class InventoryList(generics.ListCreateAPIView):
    # queryset = Inventory.objects.all()
    queryset = Inventory.objects.all()
    serializer_class = CustomInventorySerializer

class InventoryDetail(generics.ListAPIView):
    # queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

    def get_queryset(self):
        slug = self.request.query_params.get('name', None)
        return Inventory.objects.filter(name=slug)

class supplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = supplierSerializer

class supplierDetail(generics.RetrieveDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = supplierSerializer

""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""