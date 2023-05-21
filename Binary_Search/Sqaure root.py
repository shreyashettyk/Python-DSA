
#https://leetcode.com/problems/sqrtx/
#https://leetcode.com/problems/valid-perfect-square/
class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start <= end :
            mid = (start + end ) // 2
            value = mid * mid
            if value == x:
                return mid
            elif value > x:
                end = mid - 1
            else:
                start = mid + 1
        return end