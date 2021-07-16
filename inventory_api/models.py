from django.db import models

# Create your models here.
class Supplier(models.Model):
    id = models.AutoField(primary_key=True, unique = True)
    name = models.CharField(max_length=200)
  
    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    id = models.AutoField(primary_key=True, unique = True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    supplier = models.ForeignKey( Supplier, on_delete=models.CASCADE, default=1, related_name='supp')
    
    def __str__(self):
        return self.name