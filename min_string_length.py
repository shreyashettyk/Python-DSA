
#https://leetcode.com/problems/minimum-string-length-after-removing-substrings/submissions/1045319453/


class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s:
            print("Processing input ",i)
            stack.append(i)
            print("current stack is ", stack)
            if len(stack) > 1:
                var1 = stack[-2]
                var2 = stack[-1]
                print("var 1 is ",var1,"var 2 is ",var2)
                if ((var1 == "A" and var2 == "B") or (var1 == "C" and var2 == "D")):
                    stack.pop()
                    stack.pop()
            print("current stack is ",stack)
        print("the length of the stack is ",len(stack))
        return len(stack)


obj = Solution()
obj.minLength("ACBBD")