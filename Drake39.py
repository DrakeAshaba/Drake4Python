#METHOD OVERLOADING AND METHOD OVERRIDING
#A class that has two methods but with different number of arguments is known as method overloading

#Method Overriding
#A class that has two methods with the same number of arguments.

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2  = m2

    def sum(self, a = None, b = None, c = None):
        s = 0

        if a!= None and b!= None and c!= None:
            s= a + b + c

        elif a!=None and b!=None:
            s = a + b

        else:
            s = a

        return s 
    
s1 = Student(58, 69)
print(s1.sum(5))
#Method Overriding
class A:
    def show(self):
        print("In A show")

class B(A):
    pass

a1 = B()
a1.show()

#
class A:
    def show(self):
        print("In A show")

class B(A):
    def show(self):
        print("In B show")

s1 = B()
s1.show()
               