from human import Person
from houses import House, SmallTypicalHouse
from realtor import Realtor
import random

if __name__ == "__main__":
    house1 = House("158 Shevchenko str", 200, 37000)
    house2 = House("258 Franko str", 150, 45210)
    house3 = House("359 Khmelnytskyi str", 100, 30500)
    house4 = SmallTypicalHouse("65 Vahylevych str", 3750)
    andriy = Person("Andriy", 30, 35000, [])
    andriy.info()
    realtorr = Realtor("Olesya", houses=[house1, house2, house3, house4], discount=round(random.uniform(0.05, 0.15), 2))
    realtorr.steal_money()
    realtorr.provide_info_about_houses()
    realtorr.give_a_discount(house1)
    andriy.buy_a_house(house1, realtorr)
    andriy.info()
    lesya = Person("Lesya", 34, 30000, ["457 Zelena str"])
    lesya.info()
    realtorr.provide_info_about_houses()
    realtorr.steal_money()
    realtorr.give_a_discount(house2)
    lesya.buy_a_house(house2, realtorr)
    lesya.info()
    petro = Person("Petro", 28, 10000, [])
    petro.buy_a_house(house4, realtorr)
    petro.info()
    realtorr.provide_info_about_houses()
