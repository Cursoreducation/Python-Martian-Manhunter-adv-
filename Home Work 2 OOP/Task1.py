"""
1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
create an instance for each of the animal and call the unique method for it.
Determine if each of the animal is an instance of the Animals class

class Animals:
    "
    Parent class, should have eat, sleep
    "

class Animal1(Animal):
    "
    Some of the animal with 1-2 extra methods related to this animal
    "

 ...
"""


class Animal:
    def eat(self):
        print(f'{self.__class__.__name__} is eating!')

    def sleep(self):
        print(f'{self.__class__.__name__} is sleeping!')


class Dog(Animal):
    def bark(self):
        print(f"{self.__class__.__name__} is barking!")


class Cat(Animal):
    def meow(self):
        print(f"{self.__class__.__name__} is meowing!")


class Cow(Animal):
    def give_milk(self):
        print(f"{self.__class__.__name__} is giving milk!")


class Mouse(Animal):
    def run(self):
        print(f"{self.__class__.__name__} is running!")


class Python(Animal):
    def snake(self):
        print(f"{self.__class__.__name__} is snaking!")


dog = Dog()
cat = Cat()
cow = Cow()
mouse = Mouse()
python = Python()

dog.bark()
cat.meow()
cow.give_milk()
mouse.run()
python.snake()

dog.eat()
cat.sleep()
cow.eat()
mouse.sleep()
python.eat()

print(f"{isinstance(dog, Animal)}, {isinstance(cat, Animal)}, {isinstance(cow, Animal)}, {isinstance(mouse, Animal)},"
      f" {isinstance(python, Animal)}")
print("------------------------------------------------------------------------")

"""
 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
 create an instance of Centaur class and call the common method of these classes and unique.
 
 class Human:
    ""
    Human class, should have eat, sleep, study, work
    ""
 
 class Centaur(.. , ..):
    ""
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    ""
"""


class Human:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def eat(self):
        print(f"{self.age} years old {self.name} {self.last_name} is eating!")

    def sleep(self):
        print(f"{self.age} years old {self.name} {self.last_name} is sleeping!")

    def study(self):
        print(f"{self.age} years old {self.name} {self.last_name} is studying!")

    def work(self):
        print(f"{self.age} years old {self.name} {self.last_name} is working!")


class Centaur(Animal, Human):
    def defend_his_territory(self):
        print(f'{self.age} years old Centaur with name {self.name} defending his territory!')

    def walk(self):
        print(f"Centaur {self.name} is walking in the woods!")

    def eating(self):
        Human.eat(self)


centaur = Centaur("Vasyl", "Centaurus", 19)
centaur.eat()
centaur.sleep()
centaur.study()
centaur.work()
centaur.defend_his_territory()
centaur.walk()
centaur.eating()
