"""
4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
and create an HPLaptop class by using your interface.
"""
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
    def webcamera(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop, ABC):
    def __init__(self, screen_name, keyboard_name, touchpad_name, webcam_name, ports_name, dynamics_name):
        self.screen_name = screen_name
        self.keyboard_name = keyboard_name
        self.touchpad_name = touchpad_name
        self.webcam_name = webcam_name
        self.ports_name = ports_name
        self.dynamics_name = dynamics_name

    def screen(self):
        print(f'Screen: {self.screen_name}')

    def keyboard(self):
        print(f'Keyboard: {self.keyboard_name}')

    def touchpad(self):
        print(f'Touchpad: {self.touchpad_name}')

    def webcamera(self):
        print(f'Webcamera: {self.webcam_name}')

    def ports(self):
        print(f'Ports: {self.ports_name}')

    def dynamics(self):
        print(f'Dynamics: {self.dynamics_name}')


EliteBook = HPLaptop('14" (1920x1080) Full HD Multitouch', 'En, Ru', 'no info', '1 Mp (HD)',
                     '2 x USB 3.1 (3.2) Type-A, 2 x USB 3.1 (3.2) Type-C, HDMI, combined audio port', '2 dynamics')
EliteBook.screen()
EliteBook.keyboard()
EliteBook.touchpad()
EliteBook.webcamera()
EliteBook.ports()
EliteBook.dynamics()