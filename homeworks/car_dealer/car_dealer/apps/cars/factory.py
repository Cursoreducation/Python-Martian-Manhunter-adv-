import factory

class CarBrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    logo = factory.django.ImageField(color='blue')
