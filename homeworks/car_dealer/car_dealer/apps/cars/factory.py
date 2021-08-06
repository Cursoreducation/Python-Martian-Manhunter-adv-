import factory
import factory.fuzzy

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
    price = factory.fuzzy.FuzzyInteger(0,1000000)
    fuel_type_id = factory.fuzzy.FuzzyInteger(0,4)
    engine_power = factory.fuzzy.FuzzyInteger(0,1500)
    sitting_place = factory.fuzzy.FuzzyInteger(0,10)
    slug = factory.fuzzy.FuzzyText(length=12)
    number = 'АН 5434 ОО'
    doors = factory.fuzzy.FuzzyInteger(0,6)
    capacity = factory.fuzzy.FuzzyDecimal(1.0,5.0)


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