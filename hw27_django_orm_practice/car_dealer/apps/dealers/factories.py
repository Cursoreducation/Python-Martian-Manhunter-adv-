import factory


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Country'

    name = 'Spain'


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.City'

    name = 'Barcelona'
    country_id = 3


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.Dealer'

    title = 'dealer_5'
    e_mail = 'dealer_5@email.com'
    user_id = 2
    city_id = 2


class NewsLetterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealers.NewsLetter'

    email = 'test_email@email.com'
