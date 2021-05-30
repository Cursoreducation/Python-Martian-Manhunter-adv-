# 1st part of task: Composition
class Person:
    def __init__(self):
        left_arm = Arm('I\'m left')
        right_arm = Arm('I\'m right')
        self.arms = [left_arm, right_arm]


class Arm:
    def __init__(self, description):
        self.description = description


person = Person()

for arm in person.arms:
    print(arm.description)


# 2nd part of task: Aggregation
class CellPhone:

    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, screen_matrix):
        self.matrix = screen_matrix


if __name__ == '__main__':

    retina = Screen('Retina')
    iphone = CellPhone(retina)
    print(retina.matrix)
    print(iphone.screen.matrix)
