#INNER CLASS
#This is a class inside a class

class Student:

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name,self.rollno)

s1 = Student('Drake', 2)
s2 = Student('Ashaba', 3)

s1.show()
s2.show()
#OR
print(s1.name, s2.rollno)
print(s2.name, s2.rollno) 