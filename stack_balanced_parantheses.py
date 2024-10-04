class Node:
    def __init__(self,d):
        self.data = d
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None
        self.sz = 0
    def push(self,x):

        node= Node(x)
        print("the object created at node is ",node)
        node.next = self.head
        print("the next -> is present in ", node.next)
        self.head = node
        print("The value at head is ", self.head)
        self.sz += 1



    def pop(self):
        if self.sz != 0:
            self.head = self.head.next
            print("Now thehead is present at ",self.head)
            self.sz -= 1

    def get_tos(self):
        if self.sz != 0:
            return self.head.data


if __name__ == "__main__":
    mystack = MyStack()
    flag = False
    expr  = "[{(([]))}]{}"
    index = None
    paren_dict = {")":"(","]":"[","}":"{"}
    for i in range(len(expr)):

        index = i
        if expr[i] == "(" or expr[i] == "{" or expr[i] == "[":
            print(expr[i])
            mystack.push(expr[i])
            print("tos at ",mystack.get_tos())
        else:
            if paren_dict[expr[i]] == mystack.get_tos():
                mystack.pop()
            else:
                flag = True
                print("Not a balanced parantheses")
                break
    if not flag :
        print("balanced parenthesis")


