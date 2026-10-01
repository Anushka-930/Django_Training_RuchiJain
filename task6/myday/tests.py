from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductUpdateDeleteTests(TestCase):
	def setUp(self):
		self.product = Product.objects.create(
			pid=101,
			pname='Laptop',
			pprice=50000,
			poffer=10,
		)

	def test_product_can_be_updated(self):
		url = reverse('updateproduct', args=[self.product.id])

		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Laptop')

		response = self.client.post(url, {
			'pid': 102,
			'pname': 'Updated Laptop',
			'pprice': 52000,
			'poffer': 12,
		})

		self.assertRedirects(response, reverse('productlist'))
		self.product.refresh_from_db()
		self.assertEqual(self.product.pid, 102)
		self.assertEqual(self.product.pname, 'Updated Laptop')
		self.assertEqual(self.product.pprice, 52000)
		self.assertEqual(self.product.poffer, 12)

	def test_product_can_only_be_deleted_by_post(self):
		url = reverse('deleteproduct', args=[self.product.id])

		response = self.client.get(url)
		self.assertEqual(response.status_code, 405)
		self.assertTrue(Product.objects.filter(id=self.product.id).exists())

		response = self.client.post(url)
		self.assertRedirects(response, reverse('productlist'))
		self.assertFalse(Product.objects.filter(id=self.product.id).exists())
