from ArrayStackForMe import ArrayStack

def evalPostfix(expr):
    s=ArrayStack(100)

    for token in expr:
        if token in '+-*/':
            val2=s.pop()
            val1=s.pop()
            if token=='+': s.push(val1 + val2)
            elif token=='-': s.push(val1 - val2)
            elif token == '*': s.push(val1 * val2)
            elif token == '/': s.push(val1 / val2)
        else:
            s.push(float(token))

    return s.pop()

def precedence(op):
    if op=='(' or op==')': return 0
    elif op=='+' or op=='-': return 1
    elif op=='*' or op=='/': return 2
    else: return -1