from rest_framework import generics, viewsets
from rest_framework.response import Response
from inventory_api.models import Inventory, Supplier
from django.shortcuts import get_object_or_404
from .serializers import  InventorySerializer, SupplierSerializer, CustomInventorySerializer

class InventoryViewSet(viewsets.ModelViewSet):
    
    serializer_classes = {
        'list': CustomInventorySerializer,
        'retrieve': InventorySerializer,
    }

    default_serializer_class  = CustomInventorySerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

   
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Inventory, name=item)
    
    def get_queryset(self):
        return Inventory.objects.all()
