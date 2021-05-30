from abc import ABC, abstractmethod
import random


class PersonMeta(ABC):

    def __init__(self, name, age, availability_of_money, have_home=None):
        self.name = name
        self.age = age
        self.availability_of_money = availability_of_money
        self.have_home = have_home

    @abstractmethod
    def about_yourself(self):
        return NotImplementedError

    @abstractmethod
    def make_money(self):
        return NotImplementedError

    @abstractmethod
    def buy_house(self):
        return NotImplementedError


class Human(PersonMeta):

    def __init__(self, name, age, availability_of_money, have_home):
        super().__init__(name, age, availability_of_money, have_home)

    def about_yourself(self):
        if self.have_home == None:
            about_house = 'I do not have a house'
        else:
            if len(self.have_home) > 1:
                homes = ' and '.join(home.area for home in self.have_home)
                about_house = f'I have {len(self.have_home)} homes {homes}'
            else:
                about_house = f'I have a home {self.have_home[0].area}'
        return f'My name is {self.name}, I am {self.age} years old, {about_house}'

    def make_money(self):
        self.availability_of_money += 300

    def buy_house(self, realtor):
        print(f'{self.name} wants to buy house, ang go to realtor\n'
              f'Realtor try to steal money\n')
        if realtor.steal(4) == True:
            self.availability_of_money = 0
            print(f'{realtor.name} steal all money from {self.name}.')
            return

        print('Realtor did not steal money\n'
              'Continue buying house\n')
        print(f'{self.name} asks {realtor.name} to show all houses')
        look_houses = realtor.houses[:]
        while look_houses:
            good_home = random.choice(look_houses)
            if good_home.cost <= self.availability_of_money:
                print(f'{self.name} chose {good_home.area} - {good_home.cost} money\n'
                      f'Ask discount\n')
                good_home.apply_discount(realtor)
                self.availability_of_money = self.availability_of_money - good_home.cost
                if self.have_home == None:
                    self.have_home = [good_home]
                else:
                    self.have_home.append(good_home)
                realtor.houses.remove(good_home)
                print(f'{self.name} buy a house\n')
                return

            look_houses.remove(good_home)

        print(f'{self.name} does not have enough money\n')


class RealtorSingle(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            return cls._instances[cls]
        else:
            raise Exception('The class already created. Can be only one class')


class Realtor(metaclass=RealtorSingle):
    def __init__(self, name, houses, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def house_to_sell(self):
        c = 1
        for house in self.houses:
            print(f'House {c}: {house.area} - {house.cost} money')
            c += 1
        print()

    def give_discount(self, cost_of_house):
        return cost_of_house - cost_of_house * self.discount / 100

    def steal(self, number):
        if number == random.randint(0, 10):
            return True
        return False


class House:
    def __init__(self, area, cost):
        self.area = f'{area}m2'
        self.cost = cost

    def apply_discount(self, realtor):
        self.cost -= self.cost * realtor.discount / 100


house1 = House(26, 2500)
house2 = House(20, 1900)
house3 = House(32, 3900)
house4 = House(31, 4000)
house5 = House(40, 5000)
house6 = House(37, 4100)

realtor = Realtor('Andrew', [house6, house4, house2, house3, house1], 10)
bogdan = Human('Bogdan', 43, 1800, [house5])
oleg = Human('Oleg', 32, 2500, None)

print(bogdan.availability_of_money)
bogdan.buy_house(realtor)
bogdan.make_money()
bogdan.buy_house(realtor)

realtor.house_to_sell()
oleg.buy_house(realtor)
print(oleg.availability_of_money)
