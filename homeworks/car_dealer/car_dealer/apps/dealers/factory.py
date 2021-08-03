import factory

class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Country'

    name = 'США'


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Dealer'

    title = 'Новые авто'
    email = '12342w@gmail.com'
    city_id = 2
    user_id = 1


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.City'

    name = 'Львов'
    country_id = 4
