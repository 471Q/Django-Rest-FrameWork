
from rest_framework import serializers
from inventory_api.models import Inventory, Supplier


class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)
    class Meta:
        fields = ('id', 'name', 'description', 'note', 'stock', 'availability', 'supplier_name')
        model = Inventory

class CustomInventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)
    class Meta:
        fields = ('name', 'availability', 'supplier_name')
        model = Inventory


class SupplierSerializer(serializers.ModelSerializer):
     supplier = serializers.RelatedField(read_only=True)
     class Meta:
        model = Supplier
        fields = ('id', 'name')