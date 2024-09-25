#FUNCTIONS IN PYTHON
#function definition

def greet():
    print("Hello")
    print("Good Morning")

greet()

def add(x, y):
    c = x + y
    print(c)

add(5,4)

def add(x, y):
    c = x + y
    return c
result = add(5,4)
print(result)

#Calling a function that returns two values
def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d
result = add_sub(5,4)
print(result)