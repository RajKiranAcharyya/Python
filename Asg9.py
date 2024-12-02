openlist = ["[", "{", "("]
closelist = ["]", "}", ")"]


def wellbracketed(mystr):
    try:
        stack = []
        for i in mystr:
            if i in openlist:
                stack.append(i)
            elif i in closelist:
                pos = closelist.index(i)
                if (len(stack) > 0) and openlist[pos] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
    except Exception as e:
        print(f"An Error Occured:{e}")
        return False


expression = input("Enter An Expression: ")
if wellbracketed(expression):
    print("The Expression is Well Bracketed")
else:
    print("The Expression Is Not Well Bracketed")
