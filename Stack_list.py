def push(x):
    l.append(x)
def sizeof(l):
    return len(l)
def pop():
    if len(l) != 0:
        del_ele = l.pop(-1)
        print(str(del_ele)+" removed from the top of stack")
        return l
def get_tos(l):
    if len(l) != 0:
        return l[-1]

l = list()

if __name__ == "__main__":
    print("starting stack ops....")

    push(10)
    push(20)
    push(30)
    push(40)
    push(50)

    print("cuurently there are ",str(sizeof(l)),"elements in the stack")

    print("the top of the stack is at ... ",get_tos(l))

    pop()
    pop()

    print("cuurently there are ",str(sizeof(l)),"elements in the stack")

