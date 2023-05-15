# finding first occuernece in O(log n) time
l = [1, 10, 10, 10, 20, 20, 30, 40]

x = 10


def bfirstocc(arr, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if ((arr[mid] != arr[mid - 1]) or mid == 0):
                return mid
            else:
                high = mid - 1


first_index = bfirstocc(l, 0, len(l) - 1)
print("the first index is ", first_index)
