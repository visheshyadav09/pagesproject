from django.test import TestCase, SimpleTestCase
# Create your tests here.

# We use SimpleTestCase when we are not using a database and we use TestCase when we are using databse


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
