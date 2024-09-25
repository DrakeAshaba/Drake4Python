#TYPES OF VARIABLES
#Two types of Variables
# Instance and class(static) variables
#Variables defined inside init are called instance variables while the variables defined outside init are called class variables
class Car:
    wheels = 4

    def __init__(self):
        self.mil= 10
        self.com = 'BMW'

c1 = Car()
c2 = Car()

c1.mil  = 8


print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)