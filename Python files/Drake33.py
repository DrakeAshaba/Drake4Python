#TYPES OF METHODS
#Methods are like behaviour, variables store data.
#They inlcude Instance, class and static methods

#Instance Methods Acccesor methods and Mutator methods

school = "TINDIWNESI"
class student:
    def __init__(self, n1, n2,n3):
       self.n1 = n1
       self.n2 = n2
       self.n3 = n3

    def avg(self):
        return(self.n1 + self.n2 + self.n3)/3


    def info(cls):
         return cls.school

s1 = student(34,47, 32 )
s2 = student(19, 32, 12)

print(s1.avg())
print(student.info())