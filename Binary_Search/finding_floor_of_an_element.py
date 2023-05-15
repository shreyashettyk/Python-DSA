
def find_ceil(l,ele,low,high):
    while low <= high :
        mid = (low+high) // 2

        if l[mid] == ele:
            return mid
        elif l[mid] > ele :
            high = mid - 1
        else:
            low= mid + 1
    return high

if __name__ == "__main__":
    l  = [1,3,5,8,11,15,20]
    ele = int(input("enter ele "))
    low = 0
    high = len(l) -1
    index = find_ceil(l,ele,low,high)
    try:
        if index < 0 :
            print("entered ele smaller than all elements from sorted list, hence no floor exists")
        else:
            print("floor value of  {0} is {1}".format(ele,l[index]))
    except IndexError as IE:
        print("entered ele smaller than all elements from sorted list, hence no floor exists")