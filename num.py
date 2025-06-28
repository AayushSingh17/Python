import numpy as np
a= np.array([1,3,0])
# b = np.array([[1,3,0],[8,2,9]])
print(a)



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

#Indexing,Slicing,DataType Changing....


twod= np.array([[1,3,5],[4,0,2]])
print(twod[-1,-1])


oned = np.array([23,77,99])
print(oned)
print(oned[-1:1:-2])
print(oned[-1:])
print(oned[:1])
print(oned[:])


twod= np.array([[1,3,6],[4,0,2]])
print(twod[1,-1:-2])
print(twod.dtype)

newarr = twod.astype(float)
print(newarr)

newarr1 = twod.astype(bool)
print(newarr1)



#Commom creators in numpy....

print(np.zeros((2,3)))
print(np.ones((3,2)))
print(np.eye(3,3))

print(np.arange(1,20,3))
print(np.linspace(2,4,2))


twod_reshape = twod.reshape(3,2)
print(twod_reshape) #this func. will change shape of array but not change the original array 


twod_flat = twod.flatten()
print(twod_flat)


a = np.array([1,3,5])
b = np.array([20,55,33])
print(a+b)

print(a*3)

print(np.sqrt(b))



#Broadcasting...

c = np.array([[7],[2],[7]])
print(b+c)
print(b.sum())
print(b.mean())
print(twod.max(axis=0))
print(np.median(b))

# print(np.concatenate((a,b)))


a1 = np.array([[1,2],[6,7]])
a1 = np.array([[7,2],[9,7]])

# print(np.concatenate((a,b),axis=1))
# print(np.concatenate((a,b),axis=0))


arr1 = np.array([[1,2,3], [5,3,5], [8,4,3], [12,66,44], [99,55,22]])
newarr1 = np.array_split(arr1, 3,axis=1 )

print(newarr1)

#we also have the method split() available but it will not adjust  the elements when elements are less in source array for splitting, array_split() worked properly but split would fail.

x = np.where(arr1 == 4) #where() used to search in numpay array
#return thr inexes that get a match
print(x)


# arr =  np.array([6,4,8,5])
# y = np.serachsorted(arr, 7, side='right')
# print(y)

# arr2=[23,4,33,33,55,89]
# prit(np.sort(arr2))


# booleningindexing...
mask = b%5 == 0
print(b[mask])