# super() is used to access the parent class's methods.

class Vhicle:
    def start(self):
        print('Vhicle is starting.')

class Car(Vhicle):
    def start(self):
        super().start()
        print("Car engine is starting.")

class Bike(Vhicle):
    def start(self):
        super().start()
        print("Bike engine is starting.")

car1 = Car()
bike1 = Bike()

car1.start()
bike1.start()