#ANONYMOUS FUNCTIONS(LAMBDA)

#Normal functions
def square(a):
    return a*a

result = square(5)

print(result)

#Using anonymous functions
f = lambda a: a*a
result = f(5)
print(result)

f = lambda a,b: a + b
result = f(5,6)
print(result)