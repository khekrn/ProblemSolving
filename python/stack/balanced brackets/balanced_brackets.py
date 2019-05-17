def isBalanced(s):
    stack = []
    balanced = True
    index = 0
    my_dict = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    while index < len(s) and balanced:
        symbol = s[index]
        if symbol == "(" or symbol == "[" or symbol == '{':
            stack.append(symbol)
        else:
            if not stack:
                balanced = False
            else:
                peek = stack[len(stack) -1]
                value = None
                if symbol in my_dict:
                    value = my_dict[symbol]
                else:
                    balanced = False
                    stack.clear()
                if value is not None and value == peek:
                    stack.pop()
                else:
                    balanced = False
                    stack.clear()
                    break


        index = index + 1

    if balanced and not stack:
        return "YES"
    else:
        return "NO"

print(isBalanced('{{([])}}'))
print(isBalanced('{{)[](}}'))
print(isBalanced('{[()]}'))
print(isBalanced('{[(])}'))
print(isBalanced('{{[[(())]]}}'))
print(isBalanced('{(([])[])[]}'))
print(isBalanced('{(([])[])[]]}'))
print(isBalanced('{(([])[])[]}[]'))