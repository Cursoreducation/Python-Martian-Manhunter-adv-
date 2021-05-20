from abc import ABC, abstractmethod
# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class


class Animal:
    """
    Parent class, should have eat, sleep
    """
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.__class__.__name__} eats")

    def sleep(self):
        print(f"{self.__class__.__name__} sleeps")


class Cat(Animal):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """
    def meow(self):
        print(f"{self.name}: Meow!")

    def purr(self):
        print(f"{self.name}: Purr!")


class Dog(Animal):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """
    def bark(self):
        print(f"{self.name}: Bark!")

    def run(self):
        print(f"{self.name} runs")


class Parrot(Animal):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """
    def sing(self):
        print(f"{self.name}: Phew!")

    def fly(self):
        print(f"{self.name} flies")


class Snake(Animal):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """
    def crawl(self):
        print(f"{self.name} crawls")


class Fish(Animal):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """
    def swim(self):
        print(f"{self.name} swims")


if __name__ == "__main__":
    salem, vincent, chickie, nagini, aqua = Cat("Salem"), Dog("Vincent"), Parrot("Chickie"), Snake("Nagini"), Fish("Aqua")
    salem.meow()
    salem.purr()
    vincent.bark()
    vincent.run()
    chickie.sing()
    chickie.fly()
    nagini.crawl()
    aqua.swim()

    animals = [salem, vincent, chickie, nagini, aqua]
    for animal in animals:
        animal.eat()
        animal.sleep()
        print(f"{animal} is an instance of Animal class:", isinstance(animal, Animal))

# Output:
# Salem: Meow!
# Salem: Purr!
# Vincent: Bark!
# Vincent runs
# Chickie: Phew!
# Chickie flies
# Nagini crawls
# Aqua swims
# Cat eats
# Cat sleeps
# <__main__.Cat object at 0x7fa36dbb9dc0> is an instance of Animal class: True
# Dog eats
# Dog sleeps
# <__main__.Dog object at 0x7fa36dbb9a30> is an instance of Animal class: True
# Parrot eats
# Parrot sleeps
# <__main__.Parrot object at 0x7fa36dbb9760> is an instance of Animal class: True
# Snake eats
# Snake sleeps
# <__main__.Snake object at 0x7fa36dbb9700> is an instance of Animal class: True
# Fish eats
# Fish sleeps
# <__main__.Fish object at 0x7fa36dbb96a0> is an instance of Animal class: True
# 1.a. Create a new class Human and use multiple inheritance to create Centaur class,
# create an instance of Centaur class and call the common method of these classes and unique.


class Human:
    """
    Human class, should have eat, sleep, study, work
    """
    def eat(self):
        print(f"{self.__class__.__name__} is eating")

    def sleep(self):
        print(f"{self.__class__.__name__} is sleeping")

    def study(self):
        print(f"{self.__class__.__name__} is studying")

    def work(self):
        print(f"{self.__class__.__name__} is working")


class Centaur(Human, Animal):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """
    def fight(self):
        print(f"{self.__class__.__name__} fights")


if __name__ == "__main__":
    firenze = Centaur("Firenze")
    firenze.eat()
    firenze.sleep()
    firenze.fight()

# Output:
# Centaur is eating
# Centaur is sleeping
# Centaur fights

# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
# a.


class Person:
    """
    Make the class with composition.
    """
    def __init__(self):
        arm_left = Arm("This is left arm")
        arm_right = Arm("This is right arm")
        self.arms = [arm_left, arm_right]


class Arm:
    """
    Make the class with composition.
    """
    def __init__(self, message):
        self.message = message


if __name__ == "__main__":
    person = Person()
    for arm in person.arms:
        print(arm.message)

# Output:
# This is left arm
# This is right arm

# b.


class CellPhone:
    """
    Make the class with aggregation
    """
    def __init__(self, screen):
        self.screen = screen


class Screen:
    """
    Make the class with aggregation
    """
    def __init__(self, screen_type):
        self.screen_type = screen_type


if __name__ == "__main__":
    ips = Screen("IPS")
    xiaomi_redmi4a = CellPhone(ips)
    print(ips.screen_type)
    print(xiaomi_redmi4a.screen.screen_type)

# Output:
# IPS
# IPS

# 3.


class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.params = [name, last_name, phone_number, address, email, birthday, age, sex]

    def __str__(self):
        return str(self.params)


profile = Profile("Mariana", "Drozd", "0939909207", "Lviv", "mariasyad@gmail.com", "12.03.1992", "29", "female")

print(profile)

# Output:
# ['Mariana', 'Drozd', '0939909207', 'Lviv', 'mariasyad@gmail.com', '12.03.1992', '29', 'female']

# 4. * Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.


class Laptop(ABC):

    @abstractmethod
    def screen(self):
        raise NotImplementedError("The method is missing!")

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError("The method is missing!")

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError("The method is missing!")

    @abstractmethod
    def webcam(self):
        raise NotImplementedError("The method is missing!")

    @abstractmethod
    def ports(self):
        raise NotImplementedError("The method is missing!")

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError("The method is missing!")


class HPLaptop(Laptop):

    def __init__(self, model, screen_device, keyboard_device, touchpad_device, webcam_device, ports_types,
                 dynamics_device):
        self.model = model
        self.screen_device = screen_device
        self.keyboard_device = keyboard_device
        self.touchpad_device = touchpad_device
        self.webcam_device = webcam_device
        self.ports_types = ports_types
        self.dynamics_device = dynamics_device

    def screen(self):
        print(f"The screen of {self.model} laptop is {self.screen_device}")

    def keyboard(self):
        print(f"The keyboard of {self.model} laptop is {self.keyboard_device}")

    def touchpad(self):
        print(f"The touchpad of {self.model} laptop is {self.touchpad_device}")

    def webcam(self):
        print(f"The webcam of {self.model} laptop is {self.webcam_device}")

    def ports(self):
        print(f"The ports of {self.model} laptop are {self.ports_types}")

    def dynamics(self):
        print(f"The dynamics of {self.model} laptop are {self.dynamics_device}")


if __name__ == "__main__":
    laptop = HPLaptop("HP EliteBook 8760w Mobile Workstation",
                      "HP DreamColor 17.3-inch diagonal LED-backlit (1600 x 900 resolution)",
                      "HP DuraKeys", "Touchpad with on/off button, two-way scroll, gestures, three pick buttons",
                      "Optional 720p HD", "RJ-11/modem, one RJ-45/Ethernet, USB 3.0, USB 2.0, eSATA/USB 2.0 combo",
                      "SRS Premium Sound")

    laptop.screen()
    laptop.keyboard()
    laptop.touchpad()
    laptop.webcam()
    laptop.ports()
    laptop.dynamics()

# Output:
# The screen of HP EliteBook 8760w Mobile Workstation laptop is HP DreamColor 17.3-inch diagonal
# LED-backlit (1600 x 900 resolution)
# The keyboard of HP EliteBook 8760w Mobile Workstation laptop is HP DuraKeys
# The touchpad of HP EliteBook 8760w Mobile Workstation laptop is Touchpad with on/off button, two-way scroll, gestures,
# three pick buttons
# The webcam of HP EliteBook 8760w Mobile Workstation laptop is Optional 720p HD
# The ports of HP EliteBook 8760w Mobile Workstation laptop are RJ-11/modem, one RJ-45/Ethernet, USB 3.0, USB 2.0,
# eSATA/USB 2.0 combo
# The dynamics of HP EliteBook 8760w Mobile Workstation laptop are SRS Premium Sound
