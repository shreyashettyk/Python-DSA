l = [15,20,25,30,38,49,85]
x = 999

low = 0
high = len(l) - 1

def binaryfunc(low,high,x,l):
    while low <= high :
        mid = (low+high)//2

        if l[mid] == x:
            return True
        elif l[mid] < x:
            low = mid+1
        else:
            high = mid-1
    return False

binaryfunc(low,high,x, l)
