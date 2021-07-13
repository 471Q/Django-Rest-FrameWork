from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inventory.models import Inventory, Supplier
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def testViewAllItems(self):
        """
        test all objects.
        """
        url = reverse('inventory_api:list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testSingleItem(self):
        """
        test individual object.
        """
        url = reverse('inventory_api:detail')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testFilterQuery(self):

        """
        test filtered object.
        """
        url = reverse('inventory_api:detail')
        response = self.client.get(url+'?name=iot', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)