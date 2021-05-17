class Person:
    def __init__(self):
        left_arm = Arm('Extended left arm.')
        right_arm = Arm('Extended right arm.')
        self.arms = [left_arm, right_arm]
        
        
class Arm:
    def __init__(self, function):
        self.function = function


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self, screen_type):
        self.screen_type = screen_type


if __name__ == '__main__':
    person = Person()
    for arm in person.arms:
        print(arm.function)

    led = Screen('LED')
    my_phone = CellPhone(led)

    print('My phone has a', my_phone.screen.screen_type, 'screen.')