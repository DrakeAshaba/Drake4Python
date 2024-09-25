#SPECIAL VARIABLE NAME PART 2
#Different file
def fun1():
    print("from fun1")

def fun2():
    print("from fun2")

def main():
    fun1()
    fun2()
#Different file
main()

def add():
    print("Result 1 is")

def sub():
    print("Result 2 is")

    def main():
        add()
        sub()
    main()