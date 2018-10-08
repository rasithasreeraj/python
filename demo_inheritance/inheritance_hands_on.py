from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, name):
        self.name = name


@abstractmethod
def power_source(self):
    pass


class Buses(Vehicle):
    def power_source(self):
        print("{} run's on fuel".format(self.name))


class Cars(Vehicle):
    def __init__(self, is_seat_belt, name):
        self.name = name
        self.is_seat_belt = is_seat_belt

    def power_source(self):
        print("{} runs on fuel".format(self.name))

class SportsCars(Cars):
    def seater(self, seats):
        self.seats = seats
        super(SportsCars, self).__init__("Yes",self.name)
        print("{} is a {} seater".format(self.name,self.seats))


class EstateCars(Cars):
    pass  #    Estate cars come with an extension on the back, providing more boot space

class Bikes(Vehicle):
    def __init__(self, helmet, name):
        self.helmet = helmet
        self.name = name

    def power_source(self):
        print("power source is fuel")

@abstractmethod
def wheels(self):
    pass

#    Remember to use abstract method for helmets here
class PedalBikes(Bikes):
    def __init__(self, is_gear):
        self.is_gear = is_gear
        super(PedalBikes, self).__init__("Yes","Shimano")

    def power_source(self):
        print("The power source is Mechanical Energy for {}".format(self.name))

    def wheels(self):
        print("{} has 2 wheels".format(self.name))

class MotorBikes(Bikes):
    def __init__(self, noise, license_req, health):
        self.noise = noise
        self.license_req = license_req
        self.health = health
        super(MotorBikes, self).__init__("Yes","???")


class ElectricBikes(MotorBikes):
    def __init__(self, name):
        self.name = name
        super(ElectricBikes, self).__init__("Noiseless","No", "No compromise on Health")
        print("All {} ElectricBikes run using battery".format(self.name))
        #  print("This is a varient of {}".format(super(ElectricBikes.varient)))
    def power_source(self):
        print("{}'s power source is Battery".format(self.name))

    def wheels(self):
        print("{} has 3 wheels".format(self.name))

class Moped(MotorBikes):
    def __init__(self,name):
        self.name = name
        super(Moped, self).__init__("Noisy", "Yes", "Take toll on Health")

    def wheels(self):
        print("{} has 2 wheels".format(self.name))

    def power_source(self):
       print("{}'s power source is fuel".format(self.name))

ElectricBikes1 = ElectricBikes("Vintage")
Moped1 = Moped("Vespa")
MotorBikes1 = MotorBikes("Noisy","Yes","Takes a toll on Health")

PedalBikes1 = PedalBikes("Yes")
Bike1 = Bikes("Yes","Bikes")
Buses1 = Buses("Eicher")
SportsCars1 = SportsCars("Yes", "Porsche")

print(ElectricBikes1.name)
print(ElectricBikes1.__dict__)
print(ElectricBikes1.power_source())
print(ElectricBikes1.wheels())
print(Moped1.__dict__)
print(Buses1.__dict__)
print(SportsCars1.seater(2))
print(Moped1.power_source())
print(Moped1.wheels())

print(PedalBikes1.wheels())
print(Buses1.power_source())



