class Animals:

    def __init__(self, name='It', food='food'):

        self.name = name
        self.food = food

    def eat(self):
        print(f'{self.name.title()} eats {self.food}!')

    def sleep(self):
        print(f'{self.name.title()} is sleeping')
