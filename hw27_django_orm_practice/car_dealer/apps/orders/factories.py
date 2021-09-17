import factory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    first_name = 'Mariia'
    last_name = 'Horbova'
    email = 'test_email@test.com'
    phone = '+380994852381'
    car_id = 1
