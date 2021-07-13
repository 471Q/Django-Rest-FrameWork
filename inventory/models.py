from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    objects = models.Manager() #default manager

    def __str__(self):
        return self.name
    
class Inventory(models.Model):

    # class InventoryObjects(models.Manager):
    #     def get_queryset(self):
    #         return super().get_queryset()

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200 , default=name)
    description = models.CharField(max_length=200)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey( Supplier, on_delete=models.CASCADE, default=1, related_name='supp')
    objects = models.Manager() #default manager
    
    def __str__(self):
        return self.name

