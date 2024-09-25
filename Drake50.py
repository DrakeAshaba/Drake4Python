#BINARY SEARCH IN PYTHON
pos  = -1

def search(list, n):
    l = 0
    u = len(list) - 1

    while l<= u:
        mid = (l + u)//2

        if list(mid)==n:
            globals()['pos'] = mid
            return True
        else:
            if list(mid)<n:
                l = mid + 1

            else:
                u = mid - 1

    return False

dict = [4,7,8,12,45,99,102,702,10987,5666]

n = 45
if search(dict,n):
    print("Found at", pos +1)

else:
    print("Not found")