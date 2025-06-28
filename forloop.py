password = "aayu123"

# for i in range(3):
#     user = input("Enter Your Password:")
#     if user == password:
#         print("Welcome")
#         break
#     else:
#         print("Access Denied")

i=3
while i>0:
    user = input("Enter Your Password:")
    if user == password:
        print("Welcome")
        break
    else:
        print("Access Denied")
    i-=1