class Car:
    def __init__(self, engine):
        self.engine = engine


class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type


diesel = Engine('Diesel')
# our_car = Car(diesel)
print(diesel.engine_type)
# print(our_car.engine.engine_type)
