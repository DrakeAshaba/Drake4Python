#OPERATOR OVERLOADING IN PYTHON
 
a = 5
b = 6

print(a + b)

c = '5'
d = '6'

def __add___(self):
    return (c + d)

z = __add___()
print(z)