class LinProbMap: #선형 조사법
    def __init__(self, size=17):
        self.M = size
        self.table = [None] * self.M

    def hashFn(self, key):
        return key % self.M

    def insert(self, key):
        i = self.hashFn(key)
        count = self.M
        while count > 0:
            if self.table[i] is None:
                break
            i = (i + 1) % self.M
            count -= 1

        if count > 0:
            self.table[i] = key

    def search(self, key):
        i = self.hashFn(key)
        count = self.M
        while count > 0:
            if self.table[i] is None:
                return None
            if self.table[i] == key:
                return self.table[i]
            i = (i + 1) % self.M
            count -= 1
        return None

    def delete(self, key):
        i = self.hashFn(key)
        count = self.M
        while count > 0:
            if self.table[i] == key:
                self.table[i] = -1
                return
            if self.table[i] is None:
                return
            i = (i + 1) % self.M
            count -= 1


class QuadraticProbMap: #이차 조사법
    def __init__(self, size=17):
        self.M = size
        self.table = [None] * self.M

    def hashFn(self, key):
        return key % self.M

    def insert(self, key):
        i = self.hashFn(key)
        count = self.M
        j = 0

        while count > 0:
            prob_index = (i + j**2) % self.M
            if self.table[prob_index] is None:
                break
            j += 1
            count -= 1

        if count > 0:
            self.table[prob_index] = key

    def search(self, key):
        i = self.hashFn(key)
        count = self.M
        j = 0

        while count > 0:
            prob_index = (i + j**2) % self.M
            if self.table[prob_index] is None:
                return None
            if self.table[prob_index] == key:
                return self.table[prob_index]
            j += 1
            count -= 1
        return None

    def delete(self, key):
        i = self.hashFn(key)
        count = self.M
        j = 0

        while count > 0:
            prob_index = (i + j**2) % self.M
            if self.table[prob_index] == key:
                self.table[prob_index] = -1
                return
            if self.table[prob_index] is None:
                return
            j += 1
            count -= 1

# 테스트 코드
data = [1, 2, 3, 4, 11, 13, 20, 28, 30]

print("== 선형 조사법 (LinProbMap) ==")
lin_prob_map = LinProbMap()
for d in data:
    print("h(%d)=%2d" % (d, lin_prob_map.hashFn(d)), end='')
    lin_prob_map.insert(d)
    print(lin_prob_map.table)

print("2 탐색-->", lin_prob_map.search(2))
print("11 탐색-->", lin_prob_map.search(11))
print("28 탐색-->", lin_prob_map.search(28))

print("4 삭제-->", end='')
lin_prob_map.delete(4)
print(lin_prob_map.table)
print("13 삭제-->", end='')
lin_prob_map.delete(13)
print(lin_prob_map.table)

print("\n== 이차 조사법 (QuadraticProbMap) ==")
quad = QuadraticProbMap()
for d in data:
    print("h(%d)=%2d" % (d, quad.hashFn(d)), end='')
    quad.insert(d)
    print(quad.table)

print("2 탐색-->", quad.search(2))
print("11 탐색-->", quad.search(11))
print("28 탐색-->", quad.search(28))

print("4 삭제-->", end='')
quad.delete(4)
print(quad.table)
print("13 삭제-->", end='')
quad.delete(13)
print(quad.table)