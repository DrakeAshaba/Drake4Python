#Getting topten perfect squares
def topten():
    n = 1
    while n<= 10:
        sq = n*n
        yield sq
        n += 1

values = topten()

for i in values:
    print(i)

#Lets say you have a 1000 records you want to fetch from a database and you want to fecth each one of them one by one. You can use the generator.
