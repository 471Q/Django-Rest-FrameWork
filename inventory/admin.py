from django.contrib import admin
from . import models


#superuser access
admin.site.register(models.Supplier)
admin.site.register(models.Inventory)