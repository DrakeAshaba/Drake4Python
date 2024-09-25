#CLASS AND OBJECT IN PYTHON

class Computer:
     def config(self):
        print("i5, 16gb, 1TB")

a = 9
print(type(a))

a = '8'
print(type(a))

com1 = Computer()
print(type(com1))



class Computer:
    def config(self):
        print("i5, 16GB, 1TB")

com1 =  Computer()
com2 = Computer()
Computer.config(com1)
Computer.config(com1)


com1.config()
com2.config()
