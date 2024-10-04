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
    print("after object creation head...",mystack.head)
    print("after object creation sz...", mystack.sz)
    mystack.push(10)
    mystack.push(20)
    mystack.push(30)
    print("after push sz...", mystack.sz)
    print("after ,mupltiple push ops...")
    print(mystack.head)

    # mystack.pop()
    print("the number of elements are ...",mystack.sz)

    mystack.pop()
    print("number of elements after the pop is ",mystack.sz)

    print("Now the ele at the top of stack is ",mystack.get_tos())



