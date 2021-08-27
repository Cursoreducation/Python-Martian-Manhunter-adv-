import factory
from apps.users.models import CarDealerUser

USER_FACTORY_PASSWORD = 'password'


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f'username_{n}')
    password = factory.PostGenerationMethodCall('set_password', USER_FACTORY_PASSWORD)

    class Meta:
        model = CarDealerUser