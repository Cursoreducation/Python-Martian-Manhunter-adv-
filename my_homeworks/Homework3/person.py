from abc import ABC, abstractmethod


class Human(ABC):
    """
    Abstract class (interface) for :class: `Person`.
    """
    def __init__(self, name: str, age: int, money_available: float):
        """
        Constructor method
        """
        self.name = name.title()
        self.age = age
        self.money_available = money_available
        self.own_home = []

    @abstractmethod
    def get_info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, *args, **kwargs):
        raise NotImplementedError


class Person(Human):
    """
    This class represents behavior of the Person. It is inherited from abstract :class `Human`.
    :param name: name of the Person
    :type name: str
    :param age: age of the Person
    :type age: int
    :param money_available: Available amount of money in Person
    :type money_available: float
    """
    def __init__(self, name: str, age: int, money_available=0.0):
        """Constructor method"""
        super().__init__(name, age, money_available)

    def get_info(self):
        """
        Method is used to get info about Person.
        :return: printed f-string
        """
        if self.own_home:
            return print(f'Hi! My name is {self.name}, I\'m {self.age}. Currently I have {self.own_home} house')
        return print(f'Hi! My name is {self.name}, I\'m {self.age}. I don\'t have any home now!')

    def make_money(self):
        """
        Method, that shows how Person makes money
        """
        print(f'I\'m making money buy Crypto currencies trading')

    def buy_house(self, realtor, house):
        """
        This method checks if all conditions are met to buy a house, such as:
        house availability in realtor's list, successfulness of payment, if the Person has enough money,
        and whether the money would be stolen by realtor or not. Finally it calls methods to add house into
        Persons list of own houses, and remove the house from Realtors list.
        :param realtor: instance of class Realtor
        :type realtor: object
        :param house: instance of class House
        :type house: object
        :return: Method has multiple return statements, but each time it returns printed f-string
        """
        if house not in realtor.houses:
            return print(f'This house is not available for sale!')
        else:
            house.apply_discount(realtor.discount)

            if self.payment_approval(house.cost):
                print(f'House price after discount is {house.cost}')

                if realtor.steal_money():
                    return print(f'{realtor.name} has stolen your money!')

                self.add_own_house(house)
                realtor.remove_house(house)
                return print(f'{self.name} successfully bought the next {house}!')

    def add_own_house(self, house):   # Filling a list of houses are owned by Person
        """
        Method is used for adding a house object into the Person's list of own houses.
        :param house: instance of class House
        :type house: object
        :return: adds an object to the list `houses`
        """
        self.own_home.append(house)

    def payment_approval(self, house_cost: (int, float)):
        """
        Method check whether Person can purchase a house or not.
        :param house_cost: price of the house
        :type house_cost: float, int
        :return: It returns 'True' if payment successful and 'False' otherwise.
        :rtype: bool
        """
        if self.money_available >= house_cost:   # Person has enough available money to make a deal with Realtor
            self.money_available -= house_cost
            print(f'Payment from {self.name} was approved')
            return True
        print(f'{self.name} doesn\'t have enough money to buy this house')
        return False
