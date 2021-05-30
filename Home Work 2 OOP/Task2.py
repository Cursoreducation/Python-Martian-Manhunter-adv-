"""
2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
  a.
      class Person:
          ""
          Make the class with composition.
          ""
      class Arm:
          ""
          Make the class with composition.
          ""
  b.
      class CellPhone:
          ""
          Make the class with aggregation
          ""
      class Screen:
          ""
          Make the class with aggregation
          ""
"""


# a
class Person:
    def __init__(self):
        left_arm = Arm('This is left arm')
        right_arm = Arm('This is right arm')
        self.hands = [left_arm, right_arm]


class Arm:
    def __init__(self, info):
        self.info = info


our_person = Person()


for hand in our_person.hands:
    print(hand.info)


# b
class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, screen_type):
        self.screen_type = screen_type


oled = Screen('OLED')
# my_ph = CellPhone(oled)
print(oled.screen_type)
# print(my_ph.screen.screen_type)
