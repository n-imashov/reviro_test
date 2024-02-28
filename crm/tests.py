from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Store


class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.product_url = reverse('product-list')

    def test_list_products(self):
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_product(self):
        data = {
            "name": "Test Product",
            "description": "Test Description",
            "price": 10.99,
            "quantity": 50
        }
        response = self.client.post(self.product_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_retrieve_product(self):
        product = Product.objects.create(name="Test Product", description="Test Description", price=10.99, quantity=50)
        response = self.client.get(reverse('product-detail', kwargs={'pk': product.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Product')

    def test_update_product(self):
        product = Product.objects.create(name="Test Product", description="Test Description", price=10.99, quantity=50)
        update_data = {"name": "Updated Product Name", "price": 15.99}
        response = self.client.put(reverse('product-detail', kwargs={'pk': product.pk}), data=update_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_create_product(self):
        data = {"name": "Invalid Product"}
        response = self.client.post(self.product_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_update_product(self):
        product = Product.objects.create(name="Test Product", description="Test Description", price=10.99, quantity=50)
        invalid_update_data = {"name": "", "price": "invalid_price"}
        response = self.client.put(reverse('product-detail', kwargs={'pk': product.pk}), data=invalid_update_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class StoreAPITestCase(APITestCase):
    def setUp(self):
        self.store_url = reverse('store-list')

    def test_list_stores(self):
        response = self.client.get(self.store_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_store(self):
        data = {
            "name": "Test Store",
            "description": "Test Store Description",
            "locations": "Test Location",
            "hours": "Test Hours"
        }
        response = self.client.post(self.store_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Store.objects.count(), 1)

    def test_retrieve_store(self):
        store = Store.objects.create(name="Test Store", description="Test Store Description", locations="Test Location", hours="Test Hours")
        response = self.client.get(reverse('store-detail', kwargs={'pk': store.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Store')

    def test_update_store(self):
        store = Store.objects.create(name="Test Store", description="Test Store Description", locations="Test Location",
                                     hours="Test Hours")
        update_data = {"name": "Updated Store Name", "locations": "New Location"}
        response = self.client.put(reverse('store-detail', kwargs={'pk': store.pk}), data=update_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_create_store(self):
        data = {"name": "Invalid Store"}
        response = self.client.post(self.store_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_update_store(self):
        store = Store.objects.create(name="Test Store", description="Test Store Description", locations="Test Location", hours="Test Hours")
        invalid_update_data = {"name": "", "locations": ""}
        response = self.client.put(reverse('store-detail', kwargs={'pk': store.pk}), data=invalid_update_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
