import random


class RealtorMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):

    def __init__(self, name, houses: list, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def provide_info_about_houses(self):
        if self.houses is not []:
            print(f"My name is {self.name} and I'm a realtor.\n"
                  f"{self.name}: There are such houses:")
            for house in self.houses:
                print(f"- {house.address} with {house.area} sq.m. which costs ${house.cost}")

        else:
            print("There is no houses on sale!")

    def give_a_discount(self, house):
        house.apply_a_purchase_discount(self.discount)

    def steal_money(self):
        i = random.randrange(1, 10)
        if i == 1:
            print(f"The realtor {self.name} steal your money!")
            return True

    def sold_house(self, house):
        self.houses.remove(house)
