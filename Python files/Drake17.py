#KWARGS(Keyworded Variablelength Arguments)

def person(name, *data):
    print(name)
    print(data)

def person(name, **data):
    print(name)

    for i,j in data.items():
        print(i,j)

person('Drake', age = 21, city = 'Kampala', mob= 0706255662)

