from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class TestStatusView(TestCase):

    def test_status_view(self):
        request = self.client.get(
            path=reverse('status') #/status/
        )
        #assert request.status_code = 200
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.content.decode('utf-8'), 'OK')