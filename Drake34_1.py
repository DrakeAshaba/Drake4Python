class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)

    class Laptop:

        def __init__(self):
            self.brand= 'HP'
            self.cpu = 'i5'
            self.ram = '8GB'

s1 = Student('Drake', 2)
s2 = Student('Jenny', 3)

s1.show()
s2.show()

lap1 = s1.lap
lap2 = s2.lap

lap1 = Student.Laptop()
        