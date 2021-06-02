"""
1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class
"""


class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} *is eating*')

    def sleep(self):
        print(f'{self.name} *is sleeping*')


class Quadruped(Animals):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print(f'{self.name} *is running on four legs*')


class Deer(Quadruped):
    def __init__(self, name):
        super().__init__(name)

    def roar(self):
        print(f'{self.name} *is roaring*')

    def fight(self):
        print(f'{self.name} fights with their horns')


class Camel(Deer):
    def __init__(self, name):
        super().__init__(name)

    def carry_things(self):
        print(f'{self.name} can carry thing for long distances')

    def endurance(self):
        print(f'{self.name} can live without drinking water for 2 weeks')


class Llama(Camel):
    def __init__(self, name):
        super().__init__(name)

    def spit(self):
        print(f'{self.name} can spit on you if you are bad')


class Vicugna(Camel):
    def __init__(self, name):
        super().__init__(name)

    def cool_wool(self):
        print(f'{self.name} has wool that incs used it to do cool fabric')


cat = Animals('Albus')
cat.sleep()

horse = Quadruped('Spirit')
horse.run()

deer = Deer('Eliot')
deer.roar()

camel = Camel('Zephir')
camel.endurance()

llama = Llama('Orange')
llama.spit()

vicugna = Vicugna('Sparky')
vicugna.cool_wool()

cat1 = isinstance(cat, Animals)
print(cat1)
horse1 = isinstance(horse, Animals)
print(horse1)
deer1 = isinstance(deer, Animals)
print(deer1)
camel1 = isinstance(camel, Animals)
print(camel1)
llama1 = isinstance(llama, Animals)
print(llama1)
vicugna1 = isinstance(vicugna, Animals)
print(vicugna1)

"""
1.a. Create a new class Human and use multiple inheritance to create Centaur class,
 create an instance of Centaur class and call the common method of these classes and unique.
"""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} *is eating*")

    def sleep(self):
        print(f"{self.name} *is sleeping*")

    def study(self):
        print(f"{self.name} studies in LPNU")

    def work(self):
        print(f"{self.name} works in GlobalLogic")


class Centaur(Human, Quadruped):
    def __init__(self, name, age):
        super().__init__(name, age)

    def about(self):
        print(f'My name is {self.name} and I am centaurus. I am {self.age} y.o.')


centaur = Centaur('Cory', 22)
centaur.about()
centaur.run()
centaur.work()
centaur.sleep()
