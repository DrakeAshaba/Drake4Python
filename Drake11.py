#ARRAYS IN PYTHON
from  array import *
from operator import imod
vals = array('I', (5,9,8,4,2))

print(vals)


from array import *
vals = array('i',(5,9,-8, 4,2))

print(vals.buffer_info())

from array import *
vals = array('i', (5, 9,-8,4,2))
vals.reverse()

print(vals)

from array import *
vals = array('i', (5, 9,-8,4,2))

for i in range(5):
    print(vals[i])#print is part of the for loop so a tap has to be infront.

from array import *
vals = array('i', (5, 9,-8,4,2))

for i in range(len(vals)):
    print(vals[i])

from array import *
vals = array('u',['a','e','i'])
for e in vals:
    print(e)

from array import *
vals = array('i',[5,9,8,4,2])
newARR = array(vals.typecode,(a*a for a in vals))
for e in newARR:
    print(e)

for e in vals:
    print(e)

i = 0
while i<len(newARR):
    print(newARR[i])
    i+=1



