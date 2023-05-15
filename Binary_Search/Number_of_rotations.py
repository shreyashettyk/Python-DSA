# finding the number of rotations in a sorted rotated array

arr = [15, 18, 2, 5, 6, 8, 11, 12]
# arr = [2,5,6,8,11,12,15,18]

number_rotation = 0


def num_rotations():
    N = 8
    low = 0
    high = N - 1
    while low <= high:
        print("in loop")
        mid = (low + high) // 2
        #         print("mid is ",mid)
        next_value = (mid + 1) % N
        prev = (mid + N - 1) % N
        print('low, high,mid is ', low, high, mid)
        if ((arr[mid] < arr[prev]) and (arr[mid] < arr[next_value])):
            print("here we are... finally")

            ret_value = N - 1 - mid + 1
            #             print("ret value is ",ret_value)
            return ret_value
        if not (arr[mid] > arr[0]):
            print("check 1...")
            high = mid - 1
        elif not (arr[mid] < arr[N - 1]):
            print("check 2.....")
            low = mid + 1

        print('low, high is ', low, high)


number_rotation = num_rotations()
print("number rotations is ", number_rotation)
