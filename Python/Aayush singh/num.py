import numpy as np
a= np.array([1,3,0])
# b = np.array([[1,3,0],[8,2,9]])
print(a)

oned = np.array([23,77,99])
print(oned)


threed = np.array([[[1,2],[2,5],[5,8]]])
print(threed)



for i in range(1,5):
    print("*"*i)

for i in range(5,1,-1):
    print("*"*i)



    
#LAMBDA FUNCTION....

x = lambda a : a+10
print(x(5))


y = lambda a,b,c : a*b*c
print(y(2,7,9))


