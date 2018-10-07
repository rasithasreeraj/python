from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, color, price, tyrecount, name):
        self.color = color
        self.price = price
        self.tyrecount = tyrecount
        self.name = name

    @abstractmethod
    def acceleratevehicle(self):
        pass

    @abstractmethod
    def brakeVehicle(self):
        pass

    def lockvehicle(self):
        print("{} is locked now".format(self.name))


class Car(Vehicle):
    def __init__(self, color, price, name):
        super(Car, self).__init__(color, price, 4, name)


class Bike(Vehicle):
    def __init__(self, color, price, name):
        super(Bike, self).__init__(color, price, 2, name)

    def acceleratevehicle(self):
        print("{} is moving with 2 tyres in gear..".format(self.name))

    def brakeVehicle(self):
        print("{} is stopped..".format(self.name))


class HeroSplender(Bike):
    def __init__(self, color):
        super(HeroSplender, self).__init__(color, 80000, "Hero Splender")


class HondaActiva(Bike):
    def __init__(self, color):
        super(HondaActiva, self).__init__(color, 60000, "Honda Activa")

    def acceleratevehicle(self):
        print("{} Bike is moving with 2 tyres gearless..".format(self.name))


rasithasplender = HeroSplender("White")
print(rasithasplender.__dict__)
rasithasplender.acceleratevehicle()

rasithaactiva = HondaActiva("White")
print(rasithaactiva.__dict__)
rasithaactiva.acceleratevehicle()

rasithasplender.brakeVehicle()
rasithaactiva.brakeVehicle()
rasithaactiva.lockvehicle()
