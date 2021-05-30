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
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, type_of_HP, screenHP, keyboardHP, touchpadHP, webcamHP, portsHp, dynamicsHP):
        self.type_of_HP = type_of_HP
        self.screenHP = screenHP
        self.keyboardHP = keyboardHP
        self.touchpadHP = touchpadHP
        self.webcamHP = webcamHP
        self.portsHp = portsHp
        self.dynamicsHP = dynamicsHP

    def screen(self):
        print(f"Screen of HP Laptop: {self.screenHP}")

    def keyboard(self):
        print(f'Keyboard model of HP Laptop: {self.keyboardHP}')

    def touchpad(self):
        print(f"Touchpad of HP Laptop: {self.touchpadHP}")

    def webcam(self):
        print(f"Webcam model of HP Laptop: {self.webcamHP}")

    def ports(self):
        print(f" Ports type of HP Laptop: {self.portsHp}")

    def dynamics(self):
        print(f"Dynamics model of HP Laptop: {self.dynamicsHP}")


laptop = HPLaptop("HP Spectre x360 Convertible", "13.3 (1920х1080) FullHD Multitouch", "HP_MT_80XL", "HP x101ch",
                  "HP TrueVision FULL HD", "4 x USB 3.1(2 Type-A, 2 Type-C), 1 x HDMI", "HP Audio Boost 2.0")

laptop.screen()
laptop.keyboard()
laptop.touchpad()
laptop.webcam()
laptop.ports()
laptop.dynamics()
print(laptop)




