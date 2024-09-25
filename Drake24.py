#FILTER MAP REDUCE

#FILTER
num = [3, 2, 6, 8,4,6,2,9]

evens = list(filter(lambda n: n%2==0, num))
print(evens)

#MAP
#map(function,iterable)[SYNTAX]

nums = [3, 2, 6, 8,4,6,2,9]
evens = list(filter(lambda n: n%2==0, num))
doubles = list(map(lambda n: n + 2, evens))

print(evens)
print(doubles)

#REDUCE
from functools import reduce
nums = [3, 2, 6, 8,4,6,2,9]

evens = list(filter(lambda n: n%2==0, num))
doubles = list(map(lambda n : n*2, evens))
print(doubles)
sum = reduce(lambda a, b: a + b, doubles)
print(sum)