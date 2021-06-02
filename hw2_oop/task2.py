"""
2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
"""


class Person:
    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby
        arm1 = Arm(56)
        arm2 = Arm(55)
        self.arms = [arm1, arm2]


class Arm:
    def __init__(self, length):
        self.length = length


me_as_a_person = Person('Mariia', 'table tennis')
for arm in me_as_a_person.arms:
    print('My arm length is: ', arm.length)


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, screen_type):
        self.screen_type = screen_type


gorilla_glass = Screen('Gorilla Glass')
my_phone = CellPhone(gorilla_glass)
print(my_phone.screen.screen_type)