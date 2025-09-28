class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, element):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = element

        else:
            pass

    def pop(self):
        if not self.isEmpty():
            poppedElement = self.array[self.top]
            self.top -= 1
            return poppedElement

        else:
            pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]

        else:
            pass


def checkBrackets(data, dataLen):
    stack = ArrayStack(dataLen)
    stackIndex = ArrayStack(dataLen)
    lineNumber = 1

    for line in data.splitlines():
        charIndex = 1

        for character in line:
            if character in ['{', '[', '(']:
                stack.push(character)
                stackIndex.push((lineNumber, charIndex))

            elif character in ['}', ']', ')']:
                if stack.isEmpty():
                    print(f"[조건 1 위반] 오류 발생: 닫는 괄호 '{character}'에 대응하는 여는 괄호가 없습니다.")
                    print(f"오류 발생 위치: 파일의 {lineNumber}번째 라인, {charIndex}번째 문자")
                    return 1

                left = stack.pop()
                leftLine, leftChar = stackIndex.pop()

                if (character == "}" and left != "{") or \
                        (character == "]" and left != "[") or \
                        (character == ")" and left != "("):
                    print(f"[조건 2 위반] 오류 발생: 괄호 쌍이 일치하지 않습니다")
                    print(f"오류 발생 위치: 파일의 {lineNumber}번째 라인 {charIndex}번째 문자")
                    return 2

            charIndex += 1
        lineNumber += 1

    if not stack.isEmpty():
        left = stack.pop()
        leftLine, leftChar = stackIndex.pop()
        print(f"[조건 3 위반] 오류 발생: 여는 괄호 '{left}'에 대응하는 닫는 괄호가 없습니다.")
        print(f"오류 발생 위치: 파일의 {leftLine}번째 라인, {leftChar}번째 문자")
        return 3

    print("오류가 발생하지 않았습니다")
    return 0


file = open(input("file name: "), "r")
fileData = file.read()
file.close()

print("주어진 파일 괄호 쌍 일치 불일치 결과 : ")
checkBrackets(fileData, len(fileData))