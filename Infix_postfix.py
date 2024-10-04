
expr = "a+b*(c^d-e)^(f+g*h)-i"
expr_dict = {"^":3,"*":2,"/":2,"+":1,"-":1}

stack = []
postfix_output = []

def push(stack,x):
    stack.append(x)
def pop():
    pop_element = stack.pop()
    return pop_element
def peek():
    return stack[-1]
def size_stack():
    return len(stack)

for symbol in expr:
    print("the symbol is ",symbol)
    if ord(symbol) >= 97 and ord(symbol) <= 122:
        postfix_output.append(symbol)
    elif symbol == "(" or len(stack) == 0 or symbol == ")":
        stack.append(symbol)

    else:
        tos_symbol = peek()
        # if tos_symbol == "(" or tos_symbol == ")":
        #     stack.append(symbol)
        if tos_symbol != ")" and tos_symbol != "(" and expr_dict[tos_symbol] < expr_dict[symbol]:
            stack.append(symbol)
        elif tos_symbol == ")":
            while tos_symbol != "(":
                pop_ele = pop()
                postfix_output.append(pop_ele)
            pop()
        elif tos_symbol != ")" and tos_symbol != "(" and expr_dict[tos_symbol] >= expr_dict[symbol]:

            pop_ele = pop()
            postfix_output.append(pop_ele)
        else:
            print("did not enter into the stack...")
    print("stack is ",stack)



print(stack)
print(postfix_output)