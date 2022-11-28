from django.test import Client, TestCase


class VerificationTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_only_for_identified(self):
        """Only authorized users have access to the API."""
        response = self.guest_client.get('/api/gallery/')
        self.assertEqual(response.status_code, 401)
