from django.test import TestCase
from .models import Item
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class ItemModelTest(TestCase):
    def test_item_creation(self):
        item = Item.objects.create(
            name='Test Item',
            description='This is a test item.'
        )
        self.assertEqual(item.name, 'Test Item')
        self.assertEqual(item.description, 'This is a test item.')

class ItemAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item_data = {'name': 'Test Item', 'description': 'This is a test item.'}
        self.item = Item.objects.create(name='Test Item', description='This is a test item.')

    def test_api_can_get_an_item_list(self):
        response = self.client.get(reverse('item-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_create_an_item(self):
        response = self.client.post(reverse('item-list'), self.item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)