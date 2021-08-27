from django.test import TestCase
from .models import Car, Color, Brand, Model, FuelType, Property
from apps.dealers.models import Dealer, City, Country
from apps.users.factory import UserFactory


# Create your tests_car here.


class TestCarModel(TestCase):

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
        cls.color = Color.objects.create(
            name="Красный",
        )
        cls.brand = Brand.objects.create(
            name="Opel",
        )
        cls.model = Model.objects.create(
            name="Setra",
            brand_id=1,
        )
        cls.fuel_type = FuelType.objects.create(
            fuel_type=FuelType.FUEL_PETROL,
        )
        cls.car = Car.objects.create(
            slug='Opel_Setra',
            price=20000,
            number='AA 6547 ОН',
            description='The best cars',
            fuel_type_id=1,
            doors=4,
            capacity=1.5,
            sitting_place=5,
            engine_power=150,
            color_id=1,
            dealer_id=1,
            model_id=1,
        )
        cls.property1 = cls.car.category.create(
            category=Property.CATEGORY_BUS,
            name="Автобус"
        )
        cls.property2 = cls.car.category.create(
            name="Пассажирский"
        )

    def test_models_color(self):
        self.assertIsNotNone(self.color.id)
        self.assertEqual(self.color.name, "Красный")

    def test_models_model(self):
        self.assertIsNotNone(self.model.id)
        self.assertEqual(self.model.name, "Setra")

    def test_models_brand(self):
        self.assertIsNotNone(self.brand.id)
        self.assertEqual(self.brand.name, "Opel")

    def test_models_car(self):
        self.assertIsNotNone(self.car.id)
        self.assertEqual(self.car.price, 20000)
        self.assertEqual(self.car.description, 'The best cars')
        self.assertEqual(self.car.slug, 'Opel_Setra')
        self.assertEqual(self.car.engine_type, Car.ENGINE_CARBURETOR)
        self.assertEqual(self.car.population_type, Car.POPULATION_ALL)
        self.assertEqual(self.car.status, Car.STATUS_PENDING)
        self.assertEqual(self.car.gear_case, Car.GEAR_CASE_MECHANICAL)

    def test_ManyToMany_car(self):
        self.assertEqual(self.car.category.get(name="Автобус"), self.property1)
        self.assertEqual(self.car.category.get(name="Пассажирский"), self.property2)

    def test_foreign_key_car(self):
        self.assertEqual(self.car.model.name, 'Setra')
        self.assertEqual(self.car.model.brand.name, 'Opel')
        self.assertEqual(self.car.dealer.email, '123@gmail.com')
        self.assertEqual(self.car.color.name, "Красный")
        self.assertEqual(self.car.fuel_type.fuel_type, FuelType.FUEL_PETROL)
