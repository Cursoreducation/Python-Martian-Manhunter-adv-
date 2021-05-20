from abc import ABC, abstractmethod
import random


class Human(ABC):
    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self):
        raise NotImplementedError

    @abstractmethod
    def buy_a_house(self, house, realtor):
        pass


class Person(Human):
    def __init__(self, name, age, money, home: list):
        self.name = name
        self.age = age
        self.money = money
        self.home = home

    def info(self):
        print(f"My name is {self.name}. I'm {self.age} years old.\n"
              f"I have ${self.money} in my wallet.")
        if len(self.home) >= 1:
            print(f"{self.name}: I have such realty: {self.home}.")
        else:
            print(f"{self.name}: I have no realty.")

    def make_money(self):
        print(f"{self.name}: I earned some money. \n"
              f"Now I have ${self.money} in my wallet.")
        self.money += random.randrange(200, 500, 100)

    def buy_a_house(self, house, realtor):
        if realtor.steal_money is True:
            self.money -= house.cost
            print("Shit! The realtor stole my money!")
            return
        if house in realtor.houses:
            if self.money >= house.cost:
                print(f"{self.name}: I buy the house {house.address} with area {house.area} sq.m. which costs"
                      f" ${house.cost}.")
                self.money -= house.cost
                print(f"{self.name}: Now I have ${self.money}.")
                self.home.append(house.address)
                realtor.sold_house(house)
            else:
                while self.money < house.cost:
                    print(f"Can't buy this house {house.address}. I must earn more money or choose another one.")
                    print("What should we do?\n")
                    action = input("Please input '1' for earning money or '2' for choosing another one': ")
                    if action == "1":
                        self.make_money()
                    elif action == "2":
                        return
                    else:
                        print("Incorrect action! Try again!")
        else:
            return "There is no houses available"
