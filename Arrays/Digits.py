
digits = [1,2,3]
nums = digits
nums = [str(x) for x in nums]
nums = str(int(''.join(nums))+1)
k = []
for  i in nums:
    k.append(i)

k = [int(x) for x in k]
print(k)