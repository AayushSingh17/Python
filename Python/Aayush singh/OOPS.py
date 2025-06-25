# #CLASS....

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def wish(self):
#         print(f"Helo {self.name}")

# p = Person("BOB", 18)
# p.wish()

# class Animal:
#     def __init__(self, eyes, sound):
#         self.eyesAtt = eyes
#         self.soundAtt = sound
    
#     def animalSound(self):
#         print(f"The sound is {self.sound}")
        
# cat = Animal(2, "meow")
# print(cat.eyesAtt)
# cat.animalSound()


# class car:
#     def __init__(self, name, color, yom, speed):
#         self.name=name
#         self.color=color
#         self.yom=yom
#         self.speed=speed

#     def carDetails(self):
#         print(f"""The details of the car is :\n
#             Name = {self.name}
#             Color = {self.color}
#             Yom = {self.yom}
#             Speed = {self.speed}""")

# car=car("Audi", "Black", 2025, 300)
# car.carDetails()

 
# class father:
#     def fathermethod(self):
#         print("Papa ka Paisa")

# class child(father):
#     def salary(self):
#         print("Khud ki kmai")

# x = child()
# x.salary()
# x.fathermethod()

# y = father()
# y.fathermethod()
# y.salary()


class father:
    def father(self):
        print("Father")

class mother:
    def mother(self):
        print("Mother")
        

class child(father,mother):
    def myself(self):
        print("Child")

x = child()
x.father()
x.mother()
x.myself()


class Protected:
    def __init__(self):
        self._age=30

class Subclass(Protected):
    def display_age(self):
        print(self._age)

obj = Subclass()
obj.display_age()


class Private:
    def __init__(self):
        self.__salary=999999999

    def salary(self):
        return self.__salary

obj = Private()
print(obj.salary())



#Abstraction...

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car Started")

class Bike(Vehicle):
    def start(self):
        print("Bike Started")

v1=Car()
v2=Bike()
v1.start()
v2.start()



class Payment_Method(ABC):
    @abstractmethod
    def payment(self):
        pass

class UPI(Payment_Method):
    def payment(self):
        print("Payment With UPI")

class CreditCard(Payment_Method):
    def payment(self):
        print("Payment with Credit Card")

v1=UPI()
v2=CreditCard()
v1.payment()
v2.payment()


#Polymorphism

class Bird:
    def sound(self):
        print("Chirp")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

b= Bird()
c= Cat()

make_sound(b)
make_sound(c)
