import factory

class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Country'

    name = 'США'
