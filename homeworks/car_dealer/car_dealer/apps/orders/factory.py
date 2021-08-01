import factory

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    first_name = 'Serhii'
    second_name = 'Demydov'
    card_id = "2"