#INTRODUCTION TO POLYMORPHISM
#DUCKTYPING

class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()

ide = Pycharm()

Lap1 = Laptop()
Lap1.code(ide)


class VsCode:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell  Check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self):
        ide.execute()

ide = MyEditor()

Lap1 = Laptop()
Lap1.code(ide)
    
     
        