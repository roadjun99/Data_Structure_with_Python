from post_operating_system import *

def Infix2Postfix(expr):
    s=LinkedStack()
    output=[]

    for term in expr:
        if term in '(':
            s.push('(')

        elif term in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)

        elif term in "+-*/":
            while not s.isEmpty():
                op=s.peek()
                if(precedence(term)<=precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)

        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output

expr_1=list(input("입력 수식[공백 문자로 분리] = ").split())   # 과제 수행 부분
postfix_1=Infix2Postfix(expr_1)
result_1=evalPostfix(postfix_1)
print("중위 표기: ",expr_1)
print("후위 표기: ",postfix_1)
print("계산 결과: ",result_1)