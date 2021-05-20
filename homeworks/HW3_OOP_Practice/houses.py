from abc import ABC, abstractmethod


class Home(ABC):
    @abstractmethod
    def apply_a_purchase_discount(self, discount):
        raise NotImplementedError


class House(Home):
    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    def apply_a_purchase_discount(self, discount):
        if discount > 0:
            print(f"You're lucky! A discount for house {self.address} is {discount}!"
                  f"Now it costs {self.cost - round(self.cost * discount)}")
            self.cost -= round(self.cost * discount)
        else:
            print(f"Sorry, but there is no discount for house {self.address}.")


class SmallTypicalHouse(House):
    def __init__(self, address, cost, area=40):
        super().__init__(address, area, cost)
