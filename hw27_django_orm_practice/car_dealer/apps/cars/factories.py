import factory


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    number = 'BH5230BX'
    slug = 'HT'
    engine_power = 100
    dealer_id = 1
    picture_id = 1
    color_id = 1
    model_id = 1


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = 'Yellow'


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    name = 'Hyundai'


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    name = ' '


class PictureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Picture'

    position = 2
    metadata = 'Second meta'
    url = factory.django.ImageField(from_path='pictures/25493371.jpg')


class ModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Model'

    name = 'Tucson'
    brand_id = 5
