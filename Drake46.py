#FILE HANDLING IN PYTHON
f = open('My Data', 'r')

print(f.readline())
print(f.readline())

print(f.readline(), end="")

f1 = open('abc', 'w')
f1.write("Something")
f1.write('Laptop')

f1 = open('abc', 'a')
for data in f:
    f1.write(data)


f = open('')
f1 = open()
for i in f:
    print(i)