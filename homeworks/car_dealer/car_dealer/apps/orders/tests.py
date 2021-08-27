from django.test import TestCase
from apps.cars.models import Car, Color, Brand, Model, FuelType, Property
from apps.dealers.models import Dealer, City, Country
from .models import Order
from apps.users.factory import UserFactory


# Create your tests_car here.


class TestOrderModel(TestCase):

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
        cls.order = Order.objects.create(
            car_id=1,
            first_name="Serhii",
            second_name="Demydov",
            email="serjdemidov@gmail.com",
            phone="380952436261",
            message="First car",
        )

    def test_models_order(self):
        self.assertIsNotNone(self.order.id)
        self.assertEqual(self.order.first_name, 'Serhii')
        self.assertEqual(self.order.second_name, 'Demydov')
        self.assertEqual(self.order.email, 'serjdemidov@gmail.com')
        self.assertEqual(self.order.phone, '380952436261')
        self.assertEqual(self.order.message, 'First car')
        self.assertEqual(self.order.car, self.car)


