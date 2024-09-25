#RECURSION IN PYTHON 
import sys

sys.setrecursionlimit(2000)#sets the number of times a functinn is displyed on the terminal
print(sys.getrecursionlimit())#displays the limit of the display

i = 0
def greet():
    global i
    i += 1
    print("Hello", i)
    greet()

greet()

#FACTORIAL USING RECCURSION
def fact(n):
    if n==0:
        return 1
    
    return n*fact(n-1)

result = fact(5)
print(result)
