from abc import abstractmethod, ABC


class Laptop(ABC):
    def __init__(self, model):
        self.model = model

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
    def __init__(self, model, screen_size, keyboard_type, touchpad_type, webcam_type, port, dynamic):
        super().__init__(model)
        self.screen_size = screen_size
        self.keyboard_type = keyboard_type
        self.touchpad_type = touchpad_type
        self.webcam_type = webcam_type
        self.port = port
        self.dynamic = dynamic

    def screen(self):
        print(f'Screen: {self.screen_size}')

    def keyboard(self):
        print(f'keyboard: {self.keyboard_type}')

    def touchpad(self):
        print(f'touchpad: {self.touchpad_type}')

    def webcam(self):
        print(f'webcam: {self.webcam_type}')

    def ports(self):
        print(f'ports: {self.port}')

    def dynamics(self):
        print(f'dynamics: {self.dynamic}')


if __name__ == '__main__':
    hp = HPLaptop('HP', 'screen', 'keyboard', 'touchpad', 'webcam', 'ports', 'dynamics')

    print(f'{hp.model}, has characteristics:')
    hp.screen()
    hp.keyboard()
    hp.touchpad()
    hp.webcam()
    hp.ports()
    hp.dynamics()
