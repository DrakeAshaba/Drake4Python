#WORKING WITH MATRICES IN PYTHON
#Two dimensional arrays
from array import*
from numpy import*
arr1 = array([1, 2,3], [4,5,6])
print(arr1.dtype)


from numpy import*
arr1 = array([1,2,3],[4,5,6])
print(arr1.ndim)#gives the number of dimensions

print(arr1.shape)#gives the number of columns

print(arr1.size)#gives the size of the entire block

arr2 = arr1.flatten()#converts the 2d array to 1d array
print(arr2)

arr3 = arr2.reshape(3,4)#converting a single 1D array to a 3D array

arr3 = arr2.reshape(2,2,3)#2 2D arrays, 2 single arrays, each 1D has 3 values


m = matrix('1 2; 3 6; 4 5; 6 7')
print(Diagonal(m))#prints all numbers in a diagonal
print(m.max(),min())#highest and lowest

from numpy import*
m1 = matrix('1 2 3; 6 4 5; 1 6 7')
m2 = matrix('1 2 3; 6 8 5; 2 6 7')

m3 = m1 + m2 
print(m3)
