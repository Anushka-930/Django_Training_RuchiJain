from django.test import Client, TestCase


class MasterPageTests(TestCase):
    def test_home_page_renders(self):
        response = Client().get("/home/")
        self.assertEqual(response.status_code, 200)
