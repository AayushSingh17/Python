# def greet():
#     print("Hello, welcome to my channel")
# greet()

def greet(user="Guest"): #default arguement
    print(f"Hello {user}, Welcome to Python!!")

greet("Alice") #positional arguement
greet(user="Bob") #keyboard arguement
greet()

#variable length arguement (*args, **kwargs)

def greetuser(*args):
    for name in args:
        print(f"Hello,{name}!")

greetuser("Alice", "Bob", "Charlie")

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Alice",age=30, city="Paris")

def demoFunc(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)
demoFunc("a","b","c",name="Alice",age=43, city="Paris")