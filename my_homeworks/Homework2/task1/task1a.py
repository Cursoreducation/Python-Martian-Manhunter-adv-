from animals import Animals


class Human:

    def __init__(self, name='Rick', phrase='Hello!'):
        self.name = name
        self.phrase = phrase

    def eat(self):
        print(f'{self.name.title()} is eating now!')

    def sleep(self):
        print(f'{self.name.title()} is sleeping. Zzzzzzz! Zzzzzz! Zzzzz!')

    def study(self):
        print(f'{self.name.title()} is studying now')

    def work(self):
        print(f'{self.name.title()} is working now')


class Centaur(Human, Animals):

    def __init__(self, name='Unknown Centaur'):
        self.name = name
        super().__init__(self.name)

    def fight(self):
        print(f'{self.name.title()} likes to fight with knives!')


if __name__ == '__main__':

    cent = Centaur('Frank')
    cent.eat()
    cent.sleep()
    cent.fight()
