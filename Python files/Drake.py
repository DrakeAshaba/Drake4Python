#USER INPUT IN ARRAY SEARCH ELEMENTS
from array import *
arr = array('i', [])

n = int(input("Enter the length of the array:"))

for i in range(n):
    x = int(input("Enter the next value:"))
    arr.append(x)

print(arr)

array('i', [12,23,12,34])

val = int(input("Enter the value of search"))
k = 0
for e in arr:
    if e== val:
        print(k)
        break
    k+=1

    print(arr.index(val))