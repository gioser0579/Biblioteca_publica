
from django.test import TestCase
from django.urls import reverse

class PollsIndexViewTests(TestCase):
    def test_index_view_returns_200(self):
        """
        Tests that the index view returns a 200 OK status code.
        """
        url = reverse('polls:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
