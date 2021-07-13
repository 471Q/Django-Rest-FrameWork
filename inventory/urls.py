from django.urls import path
from django.views.generic import TemplateView

from inventory import views

app_name = 'inventory'

urlpatterns = [
    path('inventory', views.index, name="index"),
    path('inventory/<id>', views.detail, name="detail"),
]