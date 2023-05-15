# Binary search of array sorted in descending order


arr = [20, 17, 15, 14, 13, 12, 10, 9, 8, 4]
low = 0
high = len(arr) - 1
key = 100


def desc_binary_search():
    global low, high
    while low <= high:
        mid = (low + high) // 2
        print(low, high)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:

            low = mid + 1
        else:

            high = mid - 1
    return -1


found_status = desc_binary_search()
print("found status is ", found_status)