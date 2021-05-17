class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name} is eating animal feed')
    
    def sleep(self):
        print(f'{self.name} is sleeping')


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name} is eating food')
    
    def sleep(self):
        print(f'{self.name} is sleeping')
    
    def study(self):
        print(f'{self.name} is studing')
    
    def work(self):
        print(f'{self.name} is working')


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def about_me(self):
        print(f'Hi, my name is {self.name}, I am a {self.age} and I am a cat')
    
    @staticmethod
    def meow():
        print(f'Meow')
    
    def play(self):
        print(f'{self.name} running around the room')


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def about_me(self):
        print(f'Hi, my name is {self.name}, I am a {self.age} and I am a dog')
    
    def play(self):
        print(f'{self.name} catches a ball')


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def gives_milk(self):
        print(f'{self.name} gives milk')
    
    def eat(self):
        print(f'{self.name} chewing grass')


class Horse(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def run(self):
        print(f'{self.name} running')
    
    def eat(self):
        print(f'{self.name} chewing grass')


class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def gives_eggs(self):
        print(f'{self.name} gives_eggs')

    def eat(self):
        print(f'{self.name} pecks grain')


class Centaur(Animal, Human):
    def __init__(self, name, age):
        super().__init__(name, age)

    def about_me(self):
        print(f'I am centaur, my name {self.name} and I am runnig fast')

    def call_eat(self):
        Human.eat(self)


if __name__ == '__main__':
    barsic = Cat('Barsik', 5)
    rex = Dog('Rex', 7)
    plotva = Horse('Plotva', 4)
    burenka = Cow('Burenka', 3)
    luiza = Chicken('Luiza', 1)
    viktor = Centaur('Viktor', 35)

    barsic.play()
    rex.play()
    plotva.run()
    burenka.gives_milk()
    luiza.gives_eggs()
    viktor.about_me()
    viktor.work()
    viktor.call_eat()
    viktor.sleep()

    print('Isinstance Barsik? ', isinstance(barsic, Animal))
    print('Isinstance Rex? ', isinstance(rex, Animal))
    print('Isinstance Plotva? ', isinstance(plotva, Animal))
    print('Isinstance Burenka? ', isinstance(burenka, Animal))
    print('Isinstance Luiza? ', isinstance(luiza, Animal))
    print('Isinstance Viktor? ', 'Animal: ', isinstance(viktor, Animal), ' Human:', isinstance(viktor, Human))