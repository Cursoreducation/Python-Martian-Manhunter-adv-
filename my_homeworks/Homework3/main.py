from realtor import Realtor
from person import Person
from house import House


if __name__ == "__main__":
    # Realtors initialisation
    realtor_jack = Realtor('jack', 'Kyiv')
    realtor_john = Realtor('John', 'Lviv')
    realtor_nick = Realtor('Nick', 'Kharkiv')

    # House initialisation
    house_1 = House(location='Kyiv, Unit City', area=42.0, cost=1400000)
    house_2 = House(location='Kyiv, Riverside', area=50.0, cost=1200000)
    house_3 = House(location='Kyiv, Rybalsky', area=35.0, cost=1500000)
    house_4 = House(location='Lviv, Frankivsk\'kyj', area=46.0, cost=1300000)
    house_5 = House(location='Lviv, Halytskyi', area=65.0, cost=1400000)
    house_6 = House(location='Lviv, Lychakivskyi', area=52.0, cost=1200000)
    house_7 = House(location='Kharkiv, Slobidskyi', area=55.0, cost=1500000)
    house_8 = House(location='Kharkiv, Industrialnyi', area=51.0, cost=1300000)
    house_9 = House(location='Kharkiv, Kholodnohirskyi', area=49.0, cost=1300000)

    # Person initialisation
    elon = Person(name="Elon", age=42, money_available=2000000)
    anna = Person(name='Anna', age=41, money_available=5000000)
    james = Person(name='James', age=33, money_available=1800000)

    # Communication between realtor Jack and person Elon
    realtor_jack.add_house(house_1, house_2, house_3)
    realtor_jack.get_info()
    elon.buy_house(realtor_jack, house_2)

    # Communication between realtor John and person Anna
    realtor_john.add_house(house_4, house_5, house_6)
    realtor_john.get_info()
    anna.buy_house(realtor_john, house_6)

    # Communication between realtor John and person Anna
    realtor_nick.add_house(house_7, house_8, house_9)
    realtor_nick.get_info()
    anna.buy_house(realtor_nick, house_7)
