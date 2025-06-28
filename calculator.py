def sum(a,b):
   return a+b

def sub(a,b):
   return a-b

def div(a,b):
   return a%b

def mul(a,b):
   return a*b

total = mul(2,3)

Num1 = int(input("Enter Num 1"))

Num2 = int(input("Enter Num 2"))

op = input("Enter The Operator")

match op:
    case "+":
        print(sum(Num1,Num2))
    case "-":
        print(sub(Num1,Num2))
    case "%":
        print(div(Num1,Num2))
    case "*":
        print(mul(Num1,Num2))