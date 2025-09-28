class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def hour(self):
        return self.h

    def minute(self):
        return self.m

    def second(self):
        return self.s

    def isAM(self):
        return self.h < 12

    def isSame(self, t):
        return self.h == t.h and self.m == t.m and self.s == t.s

    def add(self, t):
        t1 = (self.h) * 3600 + (self.m) * 60 + self.s
        t2 = (t.h) * 3600 + (t.m) * 60 + t.s
        result = t1 + t2
        r_h = result // 3600
        r_m = (result // 60) % 60
        r_s = result % 60
        # 변경된 부분: f-string에 서식 지정자 (:02d) 추가
        return f'{r_h:02d}:{r_m:02d}:{r_s:02d}'

    def difference(self, t):
        t1 = (self.h) * 3600 + (self.m) * 60 + self.s
        t2 = (t.h) * 3600 + (t.m) * 60 + t.s
        result = t1 - t2
        if (result < 0):
            result = -1 * result
        r_h = result // 3600
        r_m = (result // 60) % 60
        r_s = result % 60
        # 변경된 부분: f-string에 서식 지정자 (:02d) 추가
        return f'{r_h:02d}:{r_m:02d}:{r_s:02d}'

    def trim(self):
        # trim 로직은 그대로 유지됩니다.
        if self.s >= 60:
            self.m += self.s // 60
            self.s = self.s % 60
        if self.m >= 60:
            self.h += self.m // 60
            self.m = self.m % 60
        if self.h >= 24:
            self.h = self.h % 24  # 24시간 이상일 경우를 대비해 나머지 연산으로 변경하는 것이 더 안전합니다.

        # 음수 시간에 대한 처리는 현재 로직이 복잡하여 단순화가 필요할 수 있으나,
        # 출력 형식에 대한 질문이므로 일단 그대로 두겠습니다.
        if self.h < 0:
            self.h = 24 - self.h
        if self.m < 0:
            self.h -= 1
            self.m = 60 - self.m
        if self.s < 0:
            self.s = 60 - self.s

        # 변경된 부분: f-string에 서식 지정자 (:02d) 추가
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

    def display(self):
        # 변경된 부분: %2d (공백으로 채움) 대신 %02d (0으로 채움) 사용
        print("time = %02d:%02d:%02d" % (self.h, self.m, self.s))
t_test1=Time(3,40,15)
t_test2=Time(21,30,50)
t_test3=Time(25,64,70)

print("Hour:",t_test1.hour())
print("Minute:",t_test1.minute())
print("Second:",t_test1.second())
print("오전이다. ->",t_test1.isAM())
print("둘이 똑같다. ->",t_test1.isSame(t_test2))
print("합계 =",t_test1.add(t_test2))
print("차이 =",t_test1.difference(t_test2))
print("바로 시간 정상화 =",t_test3.trim())
t_test1.display()