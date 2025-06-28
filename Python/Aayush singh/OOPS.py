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

#Runtime Polymorphism

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


#Compile Runtime

# class Point:
#     def __init__(self, x ,y):
#         self.x=x
#         self.y=y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y +           other.y)

# P1=Point(2,4)
# P2=Point(1,4)
# P3=P1+P2
# print(P3.x, P3.y)


# class Book:
#     def __init__(self, title, pages)
#         self.title=title
#         self.pages=pages

#     def __add__(self, other):
#         return self.pages + other.pages

# b1=Book("Python Introduction", 300)
# b2=Book("Harry Potter", 450)
# print(b1+b2)



# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll

#     def __eq__(self, value):
#         return self.roll == value.roll

# s1 = Student("Aayush", 44)
# s2 = Student("Aadi", 48)
# s3 = Student("Jay", 44)

# print(s1 == s3)
# print(s1 == s2)




# #File Handling...

# f = open("aayu.txt", "r")
# print(f.read())


# line1=f.readline()
# line2=f.readline()
# print(line1,line2)
# lines=f.readlines()
# for i in lines:
#     print(i.strip())

# f1=open("output.txt", "w")
# f1.write("Hello World\n")
# f1.write("Hello Aayush")

# l1=["apple\t", "guava"]
# f1.writelines(l1)


# f2=open("aayu.txt")
# f2.write("\nnew Content added")

# import os
# print(os.getcwd())

# #to print the path to same file
# print(os.path.exists("output.txt"))
# print(os.path.exists("output1.txt"))


# os.rename("output.txt", "output1.txt")



# with ope("image.jpg","rb")
#     data = f.read()


# os.remove("aayu.txt")


class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass

d = D()
d.greet()




class Test:
    count = 0

    def __init__(self):
        Test.count += 1

a = Test()
b = Test()
c = Test()
print(Test.count)




class Demo:
    def __init__(self, val):
        self.value = val

    def show(self):
        print(self.value * 2)

obj = Demo(5)
obj.show()



class Demo:
    def __init__(self, x):
        self.__x = x

    def show(self):
        print(self.__x)

d = Demo(10)
d.show()
print(d._Demo__x)