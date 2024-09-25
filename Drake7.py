av = 5
x = int(input("How many Candles do you want?"))

i = 1
while i <= x:
    if i > av:
        break

    print("Candy")
    i+=1

print("Bye")


for i in range(1, 101):
    if i%3==0:
        continue
    print(i)

print("Bye")

for i in range(1,101):
    if i%3==0 and i%5==0:
        continue
    print(i)

print("Bye")

#PASS 
for i in range(1, 101):
    if(i%2==0):
        pass
    else:
        print(i)

print("Bye")


#BREAK VS CONTINUE VS PASS


for i in range(5):
    if i==3:
        break
    print("Hello",i)

def fun():
    pass

if i==4:
    pass