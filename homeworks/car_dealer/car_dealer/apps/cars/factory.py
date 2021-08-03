import factory

class CarBrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    logo = factory.django.ImageField(color='blue')


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    color_id = 2
    dealer_id = 3
    model_id = 3
    price = 24000
    fuel_type_id = 2
    engine_power = 200
    sitting_place = 6
    slug = 'Telsa'
    number = 'АН 5434 ОО'
    doors = 5
    capacity = 0


class CarColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = 'Синий'


class CarModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Model'

    brand_id = 1
    name = 'RX-7'


class CarPropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    name = 'Для спортивных соревнований'


class CarPictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Picture'

    url = factory.django.ImageField(color='blue')
    position = 1