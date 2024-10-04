
#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    stack = []

    def removeDuplicates(self, s: str) -> str:

        stack = []

        for i in s:
            if len(stack) > 0:
                if i == stack[-1]:
                    stack.pop(-1)
                else:
                    stack.append(i)
            else:
                stack.append(i)

        final_str = ''.join(stack)
        return final_str