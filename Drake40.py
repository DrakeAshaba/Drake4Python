#ABSTRACT CLASS AND ABSTRACT METHOD
#Python does not abstract classes but we can use ABC to build Abstract classes
#ABC is Abstract Base Classes
#Methods that only have declaration and no definition are known as abstract methods

from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod

    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Its running")

com1 = Laptop()
com1.process()

class Programmer:
    def work(self):
        print("Solving Bugs")

class Whiteboard:
    def write(self):
        print("Its writing")


prog1 = Programmer()
prog1.work()

com2 = Whiteboard()
com2.write()

prog1.work(com2)