#EXCEPTION HANDLING IN PYTHON
#Types of errors
#Compile time error
#Logical error
#Run time error


a = 5
b = 0

try:
    print(a/b)
except Exception:
    print("Hey You cannot divide a number by zero.")

print("Bye")

try:
    print(a/b)
except Exception as e:
    print("Hey, You cannot divide a number by zero.")

a = 5
b = 2

try:
    print("Resource Open")
    print(a/b)
except Exception as e:
    print("Hey, You cannot divide a Number by Zero.")
finally:
    print("Resouce Closed")

a = 5 
b = 2

k = int(input("Enter a number"))
print(k)

try:
    print("Resource Open")
    print(a/b)
except ZeroDivisionError as e:
    print("Hey, You cannot divide a number by zero")

except ValueError as e:
    print("Invalid Input")

except Exception  as e:
    print("Something went wrong....")
finally:
    print("Resource closed")

