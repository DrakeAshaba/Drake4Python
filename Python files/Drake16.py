#TYPES OF ARGUMENTS
#Formal and Actual arguments


#Position Arguments
def person (name, age):
    print(name)
    print(age)

person('Drake', 21)

#Keyword Arguments
def person(name, age):
    print(name)
    print(age)

person(age = 20, name = 'Drake')

#Default Arguments
def person(name, age=18):
    print(name)
    print(age)

person('Drake')

#Variable length arguments
def sum(a, b):           # You can define a function where the variables are not fixed
    c = a + b            #You can pass more than two variables
    print(c)

sum(5,6)

def sum(a, *b):  #a is an integer value whike b is a tuple
    c = a

    for i in b:
        c = c + i

    print(c)

sum(5, 6, 34, 78)

def sum( *b):
    c = 0
    for i in b:
        c= c + i
    print(c)

sum(5,6,34,78)
