#CONSTRUCTOR AND SELF AND COMPARING OBJECTS
#Depends on the no. of variables and size of variables

#The Constructor allocates the size of the object

class Computer:
    def __init__(self):
        self.name = "Drake"
        self.age = 21

c1 = Computer()
c2 = Computer()

c1.name = 'Ashaba'

print(c1.name)
print(c2.name) 


class Computer:
    def __init__(self):
        self.name = 'Drake'
        self.age = 21

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
        
c1 = Computer()
c1.age = 30
c2 = Computer()

if c1.compare(c2):
    print("They are the same")
else:
    print("They are different")

print(c1.name)
print(c1.name)

