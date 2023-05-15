# finding last occuenrce in O(log n ) time
l = [1, 10, 10, 10, 20, 20, 30, 30, 30, 30, 40, 50, 50, 95]

x = 30


def blastocc(arr, low, high):
    while low <= high:

        mid = (low + high) // 2
        print('low : ', low, ' high: ', high, ' mid ', mid)
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if (((arr[mid] == arr[mid - 1]) and (arr[mid] != arr[mid + 1]))
                    or mid == len(arr) - 1
                    or mid == 0):
                return mid
            else:
                low = mid + 1

    return -1


low = 0
high = len(l) - 1
last_index = blastocc(l, low, high)
print("the last index is ", last_index)

