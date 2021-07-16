from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inventory_api.models import Inventory, Supplier
from django.contrib.auth.models import User


class PostTests(APITestCase):

    def testViewAllItems(self):
        """
        test front-end endpoint.
        """
        url = 'http://127.0.0.1:8000/inventory'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testSingleItem(self):
        """
        test api endpoint.
        """
        url = 'http://127.0.0.1:8000/api/inventory/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def testFilterQuery(self):

        """
        test front-end endpoint with query.
        """
        url = "http://127.0.0.1:8000/inventory/tablets"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)