# print("Hello World")
# name="Aayush"
# age=18
# print(type(name),type(age))
# a=10
# b=3
# print(a//b)
# num=6



# print(num<10) and (num%2==0)
# print(num%3==0 or num%5==0)


# x,y,z=10,30,40
# print(x)
# print(y)
# print(z)
# print(x is y)
# print(x is not y)

# subject = input("Enter The Subject You Know :")
# subject1 = input("Enter The Subject You Know1 :")
# print(subject+subject1)

# print(type(subject)
# s1="Hello"
# s2="Python"
# s3 = """My
#  name 
#  is 
#  aayush"""
# print(len(s3))



# txt="MY name is rocky"
# print("best" not in txt)
# print(txt[2:8])
# print(txt.upper())
# print(txt.title())
# print(txt.strip())
# print(txt.split())
# print(txt.lower())
# print(txt.replace('rocky', 'Aayush'))
# print(txt.join(["Singh"]))

# # print(s1+s2)
# # print(s1)
# # print(s2)



# print(txt.find("Aayush"))
# print(txt.count("aayush"))


# name="bob"
# age = 20
# print(f"My name is {name}")
# # print("My name is",name,"jhwjg")


# studentName= "Aayush"
# studentSem=3
# print(f"My name is {studentName} and study in Semester {studentSem}")

# print("My name is {} , i am in sem {}".format(studentName,studentSem))

# print("Aayush\n"*100)



# x="100"
# y=int(x)
# print(type(y))

# num1=0
# num2=1
# num3=-1
# print(bool(num1))
# print(bool(num2))
# print(bool(num3))


# num1=int(input("enter base:"))
# num2=int(input("enter power:"))
# print(num1**num2)

# marks=int(input("Enter your Marks"))
# if marks >= 90:
#     print("A")
# elif (marks>=80 & marks<90):
#     print("B")
# elif (marks>=70 & marks<80):
#     print("C")
# elif (marks>=60 & marks<70):
#     print("D")
# else:
#     print("F")



# i=1
# while i<=5:
    
#     if i==3:
#         i+=1
#         continue
        
#     print(i)
    


# import mymodule
# mymodule.num()




# try:
#     a=int(input("Enter the number 1:"))
#     b=int(input("Enter the number 2:"))
#     print(a/b)

# except ZeroDivisionError:
#     print("NOT DIVISIBLE...")

# except ValueError:
#     print("Please enter vaild number....")

try:
    a=input("Are you LOCKED IN Room---Yes/No")
    if a =="YES":
        print("OK,Someone is coming for your bhelp!!!")
    else:
        print("OK FINE")
except:
    print("OK WAIT")


    
# finally:
#     print(".")