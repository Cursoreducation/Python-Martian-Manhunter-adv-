from random import randint, uniform


class RealtorMeta(type):
    """
    A Singleton to meet condition: only one realtor for each city
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)

        if instance.__dict__['city'] not in cls._instances:
            cls._instances.update({instance.__dict__['city']: instance})
        else:
            for realtor in cls._instances:
                if realtor == instance.__dict__['city']:
                    raise Exception('There is already one realtor in this city')
        return cls._instances[instance.__dict__['city']]


class Realtor(metaclass=RealtorMeta):
    """
    A class to represent Realtor behavior. It is inherited from :metaclass `RealtorMeta`

    :param name: Name of realtor
    :type name: str
    :param city: City designation
    :type city: str
    """
    def __init__(self, name: str, city: str):
        """
        Constructor method
        """
        self.name = name.title()
        self.city = city.title()
        self._houses = []
        self._discount = round(uniform(0, 10.0), 2)     # Possible random discount in % from realtor

    def get_info(self):
        """
        Method prints info about available houses for sale
        """
        if self.houses:
            print(f'\nAvailable houses in {self.name}:')
            for house in self.houses:
                print(f'Location: {house.location}; Area: {house.area} m2; Cost: {house.cost} '
                      f'UAH; Price per m2: {house.price_per_m2} UAH')
        else:
            print('There are not houses for sale!')

    @staticmethod
    def steal_money():
        """
        Static method to generate a 10% possibility, that money would be stolen by realtor.
        :return: 'True' if realtor has stolen the money, 'False' otherwise
        rtype: bool
        """
        steal_chance = randint(1, 10)  # Determine a 10% chance to steal money
        if steal_chance == 1:
            return True
        return False

    @property
    def discount(self):
        print(f'\n{self.name} can propose you {self._discount}% discount for this house.')
        return round(self._discount / 100, 2)

    @property
    def houses(self):
        return self._houses

    def add_house(self, *args):      # Fill a list with available houses
        """
        Method adds houses(objects) to the list of available for sale houses
        :param args: objects (instances of class House)
        """
        for arg in args:
            self._houses.append(arg)

    def remove_house(self, house):   # Remove a house from list with available houses. Used when payment is done
        """
        Method removes object house from list of available houses to be sold.
        :param house: instance of class House
        :type: object
        """
        self.houses.remove(house)
