from abc import abstractmethod, ABC


class Laptop(ABC):

    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):

    def __init__(self, screen='15.6', keyboard='None', touchpad='None', webcam='1.3', ports='USB type-C', dynamics='B&O'):
        self.screensize = screen
        self.keyboard_type = keyboard
        self.touchpad_type = touchpad
        self.webcam_type = webcam
        self.ports_type = ports
        self.dynamics_type = dynamics

    def screen(self):
        print(f'{self.screensize}')

    def keyboard(self):
        print(f'{self.keyboard_type}')

    def touchpad(self):
        print(f'{self.touchpad_type}')

    def webcam(self):
        print(f'{self.webcam_type}')

    def ports(self):
        print(f'{self.ports_type}')

    def dynamics(self):
        print(f'{self.dynamics_type}')


if __name__ == '__main__':
    my_laptop = HPLaptop('14-inch, Full HD IPS 1920x1080', 'HP Durakeys with backlight', 'HP Imagepad',
                         'HP Wide Vision 720p', 'USB type-C, USB 3.0 (x2), HDMI', 'by Bang & Olufsen')

    my_laptop.screen()
    my_laptop.keyboard()
    my_laptop.touchpad()
    my_laptop.webcam()
    my_laptop.ports()
    my_laptop.dynamics()

