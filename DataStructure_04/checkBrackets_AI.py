from ArrayStackForMe import ArrayStack

def checkBrackets(data, dataLen):
    stack = ArrayStack(dataLen)
    stackIndex = ArrayStack(dataLen)
    lineNumber = 1

    for line in data.splitlines():
        charIndex = 1

        # 주석, 따옴표 안의 괄호를 구분하기 위한 장치. 기본 False이며 각 기호가 들어갈 시 True로 바뀌도록 함.
        in_single_quote = False
        in_double_quote = False
        in_comment = False

        for character in line:
            # 로직 우선순위: 주석 -> 따옴표 -> 괄호

            # 1. 이미 주석 안에 있다면, 어떤 처리도 하지 않음
            if in_comment:
                pass

            # 2. 주석이 시작되는지 확인
            elif character == '#' and not in_single_quote and not in_double_quote:
                in_comment = True

            # 3. 따옴표 상태 변경
            elif character == "'" and not in_double_quote:
                in_single_quote = not in_single_quote
            elif character == '"' and not in_single_quote:
                in_double_quote = not in_double_quote

            # 4. 위의 모든 조건에 해당하지 않을 때만 (즉, 실제 작동하는 코드일 때만) 괄호 검사
            elif not in_single_quote and not in_double_quote:
                if character in ['{', '[', '(']:
                    stack.push(character)
                    stackIndex.push((lineNumber, charIndex))
                elif character in ['}', ']', ')']:
                    if stack.isEmpty():
                        print(f"Error:01 | 닫는 괄호 '{character}'에 대응하는 여는 괄호가 없습니다.")
                        print(f"오류 위치: 라인 {lineNumber}, 문자 {charIndex}")
                        return 1

                    left = stack.pop()
                    leftLine, leftChar = stackIndex.pop()

                    if (character == "}" and left != "{") or \
                            (character == "]" and left != "[") or \
                            (character == ")" and left != "("):
                        print(f"Error:02 | 괄호 쌍이 일치하지 않습니다.")
                        print(f"오류 위치: 라인 {lineNumber}, 문자 {charIndex}")
                        return 2

            charIndex += 1
        lineNumber += 1

    if not stack.isEmpty():
        left = stack.pop();
        leftLine, leftChar = stackIndex.pop()
        print(f"Error:03 | 여는 괄호 '{left}'에 대응하는 닫는 괄호가 없습니다.")
        print(f"오류 위치: 라인 {leftLine}, 문자 {leftChar}")
        return 3

    print("검사 완료: 오류가 발견되지 않았습니다!")
    return 0

filename=input("file name : ")  # 임의의 Python 소스 파일 입력
with open(filename,"r") as infile:  # 더 안전한 읽기
    str = infile.read()
    print("source file", filename, " ---> ", checkBrackets(str,len(str)))