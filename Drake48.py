#LINEAR SEARCH IN PYTHON
#Searching for an element from a list
def search(lst, n):
    i = 0
    while i<len(lst):
        if lst(i)==n:
            return True
        i = i + 1

    return False

lst = [5,8,4,6,9,2]
n = 9
if search(lst,n):
    print("Found")
else:
    print("Not found")