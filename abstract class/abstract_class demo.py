# Hands on on abstract_class

from abc import ABC, abstractclassmethod


class sampleabstractclass(ABC):
    def __init__(self, fname,sname):
        self.fname = fname
        self.sname = sname
        print("{}.{}@yahoo.com is my email address".format(self.fname,self.sname))

email1 = sampleabstractclass("rasitha","sreeraj")

words =['cat','moon','dog']
for w in words:
    print(w, len(w))

words =['cat','moon','dog']
for w in words[:]:   #  Loop over a slice copy of the entire list.
    if len(w)>3:
        words.insert(0,w)
print(words)
print(words[:])  #  This statement will print the entire values inside list "words"

#  Looping techniques
questions = ['name', 'age', 'hobby']
answers = ['abc', '21', 'reading']
for q,a in zip(questions, answers):
    print("What's your {}? it is {}.".format(q,a))

#  Printing odd numbers
for i in range(1,10,2):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for b in sorted(set(basket)):  #  if set key word is not used it will display duplicates
    print(b)  #  also sorted() will not alter the original list unlike sort()

a = list(range(1,10,2))
print(a)


class Amphibian:
    def __init__(self, name, is_water, is_land):
        self.name = name
        self.is_water = is_water
        self.is_land = is_land
        #Water_living.__init__(self, is_water, self.name)
#       Land_living.__init__(self, is_land, self.name)

    def sample(self):
        if (amp1.is_water == "Yes" and amp1.is_land == "Yes"):
            return ("I am an Amphibian")
        else:
            return ("{} is not an Amphibian".format(self.name))

amp1 = Amphibian("Elephant","No","Yes")
print(amp1.__dict__)
print(amp1.sample())

#  To Take input within the class, e.g. using a class method:
#
# class StackOverflowUser:
#
#     def __init__(self, name, userid, rep):
#         self.name = name
#         self.userid = userid
#         self.rep = rep
#
#     @classmethod
#     def from_input(cls):
#         return cls(
#             raw_input('Name: '),
#             int(raw_input('User ID: ')),
#             int(raw_input('Reputation: ')),
#         )
# then call it like:
#
# user = StackOverflowUser.from_input()
#  https://stackoverflow.com/questions/32721580/example-of-class-with-user-input

