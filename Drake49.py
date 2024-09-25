pos = -1
def search(list,n):
i = 0
while i< len(list):
    if list[i] == n:
      globals()['pos'] = 1
    return True
    
    i = i + 1
   
return False

list = [5, 8, 4, 6, 9, 2]
n = 9

if search(list, n):
   print("Found at", pos)

else:
   print("Not found")
   
