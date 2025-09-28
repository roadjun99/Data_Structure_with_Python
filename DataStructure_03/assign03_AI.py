class Polynomial:
    def __init__(self, coef=[]):
        # 계수 리스트를 직접 받아 초기화할 수 있도록 변경
        self.coef = list(coef)

    def read(self):
        # 사용자로부터 입력을 받아 다항식을 설정
        n = int(input("다항식 최고 차수 입력 :"))
        temp_coef = []
        for i in range(n, -1, -1):
            coef_el = int(input(f"x^{i}의 계수 :"))
            temp_coef.append(coef_el)
        temp_coef.reverse()
        self.coef = temp_coef

    def degree(self):
        # 다항식의 최고 차수 반환
        return len(self.coef) - 1

    def evaluate(self, scalar):
        # 주어진 값(scalar)에 대한 다항식의 결과값 계산
        coef_ev_sum = 0
        for i in range(len(self.coef)):
            coef_ev_sum += self.coef[i] * (scalar ** i)
        return coef_ev_sum

    def add(self, rhs):
        # 💡 [수정된 부분]
        # 1. 결과값을 저장할 새로운 Polynomial 객체 생성
        result = Polynomial()

        # 2. 두 다항식 중 더 긴 길이(높은 차수)를 찾음
        max_len = max(len(self.coef), len(rhs.coef))

        # 3. 결과 리스트를 0으로 초기화
        result.coef = [0] * max_len

        # 4. self의 계수를 결과에 더함
        for i in range(len(self.coef)):
            result.coef[i] += self.coef[i]

        # 5. rhs의 계수를 결과에 더함
        for i in range(len(rhs.coef)):
            result.coef[i] += rhs.coef[i]

        return result

    def sub(self, rhs):
        # 빼는 다항식의 모든 계수의 부호를 바꾼 뒤 더하기 연산 수행
        neg_rhs = Polynomial([-x for x in rhs.coef])
        return self.add(neg_rhs)

    def multiply(self, rhs):
        # 두 다항식의 곱셈 결과 반환
        result = Polynomial()
        result.coef = [0] * (self.degree() + rhs.degree() + 1)
        for i in range(len(self.coef)):
            for j in range(len(rhs.coef)):
                result.coef[i + j] += self.coef[i] * rhs.coef[j]
        return result

    def display(self, message=""):
        # 💡 [개선된 부분] 출력을 더 자연스럽게 개선
        if not self.coef:
            return message + "0"

        parts = []
        # 최고차항부터 낮은 차수 순으로 처리
        for i in range(len(self.coef) - 1, -1, -1):
            coef = self.coef[i]
            if coef == 0:
                continue

            # 부호 처리 (첫 항이 아닐 경우에만)
            sign = ""
            if len(parts) > 0:
                sign = " + " if coef > 0 else " - "
            elif coef < 0:
                sign = "-"

            # 계수 처리 (절대값으로)
            num = abs(coef)
            coef_str = str(num) if (num != 1 or i == 0) else ""

            # 변수 및 차수 처리
            if i > 0:
                var_str = f"x^{i}" if i > 1 else "x"
            else:
                var_str = ""

            parts.append(f"{sign}{coef_str}{var_str}")

        return message + "".join(parts)


# --- 실행 부분 ---
a = Polynomial()
b = Polynomial()

print("- 다항식 A 정보 입력 -")
a.read()
print("\n- 다항식 B 정보 입력 -")
b.read()

# a와 b는 변경되지 않고, 연산 결과가 c, d, e에 저장됨
c = a.add(b)
d = a.sub(b)
e = a.multiply(b)

print("\n--- 결과 ---")
print(f"A(x)의 최고 차수: {a.degree()}")
print(f"A(2)의 값: {a.evaluate(2)}")
print(a.display("A(x) = "))
print(b.display("B(x) = "))
print(c.display("C(x) = A(x) + B(x) = "))
print(d.display("D(x) = A(x) - B(x) = "))
print(e.display("E(x) = A(x) * B(x) = "))