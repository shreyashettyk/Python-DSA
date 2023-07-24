#https://leetcode.com/problems/buy-two-chocolates/submissions/
#https://leetcode.com/problems/buy-two-chocolates/post-solution/?submissionId=1002248735



class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        choco_1,choco_2 = prices[0],prices[1]
        if choco_1 + choco_2 <= money:
            return money - (choco_1 + choco_2)
        else:
            return money