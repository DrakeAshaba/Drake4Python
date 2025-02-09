#MULTITHREADING IN PYTHON
#Threads

class Hello:
    def run(self):
        for i in range(5):
            print("Hello")

class Hi:
    def run(self):
        for i in range(5):
            print("Hi")

t1 = Hello()
t2 = Hi()

t1.run()
t2.run()

from time import sleep
from threading import*

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi:
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.2)

t2.start()

t1.join()
t2.join()

print("Bye")

