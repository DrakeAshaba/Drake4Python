#GLOBAL KEYWORDS IN PYTHON
#Scope
a = 10
def something():
    a = 15
    b = 8
    print(a)
    print(b)


    a = 10
    def something():
        a = 15
        print("in fun", a)
    
    something()

print("outside",a)

a = 10
print(id(a))

def something():
    a = 9
     
    x = globals()['a']
    print(id(x))
    print("in fun", a)
    globals()['a'] = 15