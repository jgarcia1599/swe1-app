from django.test import Client, TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page_loads(self):
        """Test that index page loads successfully"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to My Django App")
        self.assertContains(response, "Polls Application")
