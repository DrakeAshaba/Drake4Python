#GENERATORS IN PYTHON
#These are like built in iterators

def topten():
    yield 1
    yield 2
    yield 3
    yield 4

value = topten()

print(value.__next__())
for i in value:
    print(i)