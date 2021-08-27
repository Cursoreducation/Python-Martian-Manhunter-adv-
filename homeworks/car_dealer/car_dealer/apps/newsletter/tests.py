from django.test import TestCase

from .models import Subscribers


# Create your tests_car here.

class TestSubscribersModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.subscribers=Subscribers.objects.create(
            email="1234@gamil.com",
        )


    def test_models_dealer(self):
        self.assertIsNotNone(self.subscribers.id)
        self.assertEqual(self.subscribers.email, '1234@gamil.com')





