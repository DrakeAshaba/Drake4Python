#COPYING AN ARRAY IN PYTHON
from array import*
from numpy import*

arr = array([1,2,3,4])
arr = arr + 5
print(arr)


from numpy import*
arr1 = array([1,2,3,4,5])
arr2 = array([6,1,9,3,2])

arr3 = arr1 + arr2
print(arr3)

from numpy import*
arr1 = array([1,2,3,4,5])
print(log(arr1))
print(sqrt(arr1))
print(sum(arr1))

print(concatenate([arr1,arr2]))

from numpy import*
arr1 = array([2,6,8,1,3])
arr2, arr2
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


from numpy import*
arr1 = array([2,6,8,1,3])
arr2 = arr1.view()#copies the same array but gives it a different address
print(arr1)
print(arr2)

from numpy import*
arr1 = array([2,6,8,1,3])
arr2 = arr1.copy()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))