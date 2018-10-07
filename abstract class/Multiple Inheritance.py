class Water_living:
    def __init__(self, is_water, name):
        self.name = name
        self.is_water = is_water



class Land_living:
    def __init__(self, is_land, name):
        self.name = name
        self.is_land = is_land


class Amphibian(Water_living, Land_living):
    def __init__(self, name, is_water, is_land):
        self.name = name
        Water_living.__init__(self, is_water, self.name)
        Land_living.__init__(self, is_land, self.name)

    def sample(self):
        if (Mammal1.is_water == "Yes" and Mammal1.is_land =="Yes"):
            return ("{} is an Amphibian.".format(self.name))
        else:
            return ("{} is not an Amphibian.".format(self.name))

Water_living1 = Water_living("Yes","Fish")
Land_living1 = Land_living("Yes","Elephant")
Mammal1 = Amphibian("Tortoise","Yes","Yes")
Amphibian2 = Amphibian("Frog","Yes","Yes")
print(Mammal1.sample())

print(Water_living1.is_water)
print(Mammal1.is_water)

print(Mammal1.__dict__)
print(Water_living1.__dict__)
print(Land_living1.__dict__)


print(Amphibian.mro()) #  Will display Method Resolution Order

https://www.python-course.eu/python3_multiple_inheritance.php