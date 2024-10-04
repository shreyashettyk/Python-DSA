class Solution:
    def countStudents(self, students, sandwiches) -> int:
        for i in range(len(students)):
            print("i is ",i)
            if students[i] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(i)
            else:
                if len(students) > 1:
                    x = students.pop(i)
                    students.append(x)
                else:
                    break
            print("Students entry.. ",students)
        return len(students)

obj = Solution()
obj.countStudents([1,1,0,0],[0,1,0,1])




