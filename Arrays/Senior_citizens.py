# https://leetcode.com/problems/number-of-senior-citizens/submissions/
# https://leetcode.com/problems/number-of-senior-citizens/post-solution/?submissionId=1002253647

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for passeger_data in details:
            age = int(passeger_data[11:13])
            if age > 60:
                cnt += 1
        return cnt