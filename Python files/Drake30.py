#......INIT.....METHOD
class Computer:
    def ___init___(self,cpu,RAM):
        self.cpu = cpu
        self.RAM = RAM
    
    def config(self):
        print("Config is", self.cpu, self.RAM)


com1 = Computer()
com2 = Computer()

com1.config()
com2.config()