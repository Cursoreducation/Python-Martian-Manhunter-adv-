from abc import ABC, abstractmethod
from random import randint


class Human(ABC):
    @abstractmethod
    def provide_information(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, *args, **kwargs):
        raise NotImplementedError


class Person(Human):
    def __init__(self, name, age, availability_of_money, home_having=[]):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.home_having = home_having

    def provide_information(self):
        print(f'\nPersonal info\n'
              f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Availability of money: {self.availability_of_money}\n'
              f'Having own home:')
        for house in self.home_having:
            print(self.home_having.index(house), ' : ', {str(house)})

    def make_money(self, salary):
        print(f'Person has ', self.availability_of_money)
        self.availability_of_money += salary
        print(f'{self.name} worked and made ', salary, 'amount of money.')

    def buy_house(self, house, realtor):
        print(f'{self.name} has {self.availability_of_money} and wants to buy a house.')
        if house in realtor.houses:
            if house.cost <= self.availability_of_money:
                if realtor.steal_money() <= 10:
                    self.availability_of_money -= house.cost
                    print(f'Realtor {realtor.name} cheated, stole {house.cost} and ran away!')
                else:
                    print(f'Realtor {realtor.name} is a good guy, he don\'t steal :)')
                    realtor.houses.remove(house)
                    self.availability_of_money -= house.cost
                    self.home_having.append(house)
                    print(f'{self.name} now has a house!')
            else:
                print(f'{self.name} doesn\'t have amount of money to buy a house -_-')
        else:
            print('Realtor don\'t have this house to propose it')


class Home(ABC):
    @abstractmethod
    def apply_discount(self, *args, **kwargs):
        raise NotImplementedError


class House(Home):
    def __init__(self, cost, area):
        self.cost = cost
        self.area = area

    def apply_discount(self, discount):
        self.cost *= (1 - discount / 100)

    def __str__(self):
        return f'Cost of a house {self.cost} Area of a house {self.area} sq/m'


class SmallHouse(House):
    def __init__(self, cost, area=40):
        super().__init__(cost, area)


class RealtorMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, discount, houses=[]):
        self.name = name
        self.discount = discount
        self.houses = houses

    def provide_info_about_houses(self):
        print(f'\nRealtor {self.name} sells such houses:')
        for house in self.houses:
            print(self.houses.index(house), ' : ', {str(house)})

    def give_discount(self, house):
        if house in self.houses:
            print(f'Full price of a house: {house.cost}\n'
                  f'Discount amount: {self.discount}')
            house.apply_discount(self.discount)
            print(f'Price with discount: {house.cost}')

    @staticmethod
    def steal_money():
        return randint(0, 100)


if __name__ == "__main__":
    house01 = House(25000, 60)
    house02 = SmallHouse(10000, )
    house03 = House(15000, 55)
    house04 = House(70000, 150)
    house05 = House(130000, 200)

    person01 = Person('John', 25, 150000, [house02])
    person01.provide_information()

    realtor01 = Realtor('James', 10, [house01, house03, house04, house05])
    realtor01.provide_info_about_houses()

    person01.buy_house(house03, realtor01)
    person01.buy_house(house01, realtor01)
    person01.buy_house(house04, realtor01)
    person01.buy_house(house05, realtor01)
    realtor01.give_discount(house05)
    person01.make_money(70000)
    person01.provide_information()


