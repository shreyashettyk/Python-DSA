
def find_ceil(l,ele,low,high):
    if ele > l[len(l) - 1]:
        return -1
    while low <= high :
        mid = (low+high) // 2
        if l[mid] > ele :
            high = mid - 1
        elif l[mid] < ele:
            low= mid + 1
    return low

if __name__ == "__main__":
    l  = ['a','c','d','f']
    ele = str(input("enter char "))
    low = 0
    high = len(l) -1
    index = find_ceil(l,ele,low,high)
    if index < 0 :
        print("the ciel value of {0} is {1} ".format(ele,l[0]))
    else:
        print("ceil value of  {0} is {1}".format(ele,l[index]))
