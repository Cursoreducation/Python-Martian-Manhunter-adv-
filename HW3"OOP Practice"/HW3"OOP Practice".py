"""
There is a Person whose characteristics are:
1. Name
2. Age
3. Availability of money
4. Having your own home

Human can:
1. Provide information about yourself
2. Make money
3. Buy a house

There is also a House, the properties of which include:
1. Area
2. Cost

For Home you can:
1. Apply a purchase discount

e.g.: There is also a Small Typical House with a required area of 40m2.

*Realtor:
1. Name
2. Houses
3. Discount that he/she can give you.

*There is only one realtor who handles small houses you wanna buy. (Singleton)
Realtor is only one in your city and can:
1. Provide information about all the Houses
2. Give a discount
3. Steal your money with 10% chance
"""
from abc import ABC, abstractmethod
import random


class Human(ABC):
    @abstractmethod
    def info_about_person(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, house):
        raise NotImplementedError

    @abstractmethod
    def income(self, flowers, price):
        raise NotImplementedError


class Person(Human):
    def __init__(self, name, age, own_money, salary,  his_house=None):
        if his_house is None:
            his_house = []
        self.name = name
        self.age = age
        self.own_money = own_money
        self.salary = salary
        self.his_house = his_house

    def info_about_person(self):
        print(f'Hi! My name is {self.name}. I am {self.age} years old. I have {self.own_money} dollars')

    def make_money(self):
        print(f"\tI have {self.own_money} dollars")
        self.own_money = self.own_money + self.salary
        print(f'\tBut I got my salary {self.salary} and now i have {self.own_money} dollars')

    def buy_house(self, house):
        if self.own_money < house.cost:
            print("Ohhh... I do not the required amount of money. So, I heed to wait for the salary or earn")
        else:
            self.own_money = self.own_money - house.cost
            print(f"Yeeees, I bought a dream house. The price of the house - {house.cost}. Now i have left "
                  f"{self.own_money} dollars :(")

    def income(self, flowers, price=10):
        if flowers > 25:
            self.own_money = self.own_money + (price * flowers)
            print(f'{self.name} sold flowers and earned. He has {self.own_money} dollars!')


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def discount(self, discount):
        if self.area >= 100:
            self.cost = (1 - discount / 100) * self.cost
            print(f"There is a {discount}% discount on this house!")


class RealtorMeta(type):
    _instances = {}

    def call(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().call(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMeta):
    def __init__(self, name, discount, houses=None):
        if houses is None:
            houses = []
        self.name = name
        self.discount = discount
        self.houses = self.house_list(houses)

    def house_list(self, houses):
        house_list = []
        for house in houses:
            house_list.append(house)
        return house_list

    def info_about_houses(self):
        if self.houses:
            print(f'Hello, my name is {self.name}! I am a realtor!!!')
            for house in self.houses:
                print(f'These house on sale: {house}')
        else:
            print('Sorry, but we do not a vacant houses')

    def give_discount(self):
        return self.discount

    def steal_money(self):
        return random.randrange(0, 101)


if __name__ == '__main__':
    person_instance = Person("Maks", 19, 30000, 2000)
    house_instances1 = House(101, 35000)
    house_instances2 = House(120, 42000)
    house_instances3 = House(90, 29550)
    house_instances4 = House(79, 26650)
    house_instances5 = House(100, 33680)
    realtor_instance = Realtor("Yevheniy", 0.15, [house_instances1, house_instances2, house_instances3, house_instances4,
                                                  house_instances5])
    person_instance.info_about_person()
    person_instance.make_money()
    person_instance.income(150)
    realtor_instance.info_about_houses()
    realtor_instance.give_discount()
    person_instance.buy_house(house_instances5)
    person_instance.income(100)
    person_instance.buy_house(house_instances5)
