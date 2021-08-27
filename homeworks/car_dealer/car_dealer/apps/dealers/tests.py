from django.test import TestCase

from .models import Dealer, City, Country
from apps.users.factory import UserFactory


# Create your tests_car here.


class TestDealerModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.country = Country.objects.create(
            name="Ukraine"
        )
        cls.city = City.objects.create(
            name="Kyiv",
            country_id=1,
        )
        cls.dealer = Dealer.objects.create(
            title='Продажа авто',
            email='123@gmail.com',
            city_id=1,
            user_id=1,
        )

    def test_models_country(self):
        self.assertIsNotNone(self.country.id)
        self.assertEqual(self.country.name, "Ukraine")

    def test_models_city(self):
        self.assertIsNotNone(self.city.id)
        self.assertEqual(self.city.name, "Kyiv")
        self.assertEqual(self.city.country.name, "Ukraine")

    def test_models_dealer(self):
        self.assertIsNotNone(self.dealer.id)
        self.assertEqual(self.dealer.title, 'Продажа авто')
        self.assertEqual(self.dealer.email, '123@gmail.com')
        self.assertEqual(self.dealer.city.name, "Kyiv")
        self.assertEqual(self.dealer.city.country.name, "Ukraine")




