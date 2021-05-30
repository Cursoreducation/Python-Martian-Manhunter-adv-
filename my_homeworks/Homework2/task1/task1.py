from animals import Animals


class Dog(Animals):

    def __init__(self, name='some dog', breed='mongrel'):
        super().__init__(name)
        self.breed = breed
        self.food = 'meat'

    def bark(self):
        print(f'The {self.name.title()} barks!')

    def get_info(self):
        print(f'This is {self.name.title()}, and it is a {self.breed}!')


class Cat(Animals):

    def __init__(self, name='some cat'):
        super().__init__(name)
        self.food = 'fish'

    def meow(self):
        print(f'{self.name.title()} makes Meow!!!')

    @staticmethod
    def make_mur():
        print('Mrrrrrrr')


class Fish(Animals):

    def __init__(self, name='Frank'):
        super().__init__(name)
        self.food = 'plankton'

    def swim(self):
        print(f'{self.name.title()} swims')


class Bird(Animals):

    def __init__(self, name='Garry'):
        super().__init__(name)
        self.food = 'worms'

    def fly(self):
        print(f'{self.name.title()} fly\'s')


class Snake(Animals):

    def __init__(self, name='Johny'):
        super().__init__(name)
        self.food = 'students'

    def creep(self):
        print(f'{self.name.title()} is creeping! Be careful!)')


if __name__ == '__main__':

    my_dog = Dog()
    my_cat = Cat()
    my_fish = Fish()
    bird = Bird()
    python = Snake()

    my_dog.bark()
    my_dog.get_info()
    my_dog.eat()
    my_cat.meow()
    my_cat.make_mur()
    my_fish.swim()
    bird.fly()
    python.creep()
    python.eat()

    common_animals_list = [my_dog, my_cat, my_fish, bird, python]

    for my_animal in common_animals_list:
        print(f'\n Instance of class Animals? {isinstance(my_animal, Animals)}')
