#https://leetcode.com/problems/contains-duplicate-ii/
def containsNearbyDuplicate(nums,k) :
    i = 0
    j = 1
    while j < len(nums):
        if not k:
            return False
        if (nums[i] != nums[j]) and (j - i <= k):
            # print(i,j)
            j += 1
        else:
            if (nums[i] == nums[j]) and (j - i <= k):
                # print(i,j)
                return True
            else:

                i += 1

    if j >= len(nums):
        # print(i,j)
        return False



nums = [0,1,2,3,2,5]
k = 3

val = containsNearbyDuplicate(nums,k)
print(val)