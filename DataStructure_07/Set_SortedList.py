class SetSorted:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def contains(self, item):
        left, right = 0, self.size() - 1
        while left <= right:
            mid = (left + right) // 2
            if self.items[mid] == item:
                return True
            elif self.items[mid] < item:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def insert(self, item):
        if self.contains(item):
            return
        self.items.append(item)

        for i in range(self.size() - 1, 0, -1):
            if self.items[i - 1] <= self.items[i]:
                break
            self.items[i - 1], self.items[i] = self.items[i], self.items[i - 1]

    def delete(self, item):
        if not self.contains(item):
            return
        self.items.remove(item)

    def display(self, msg):
        print(msg, self.items)

    def __eq__(self, setB):
        if self.size() != setB.size():
            return False
        for i in range(self.size()):
            if self.items[i] != setB.items[i]:
                return False
        return True

    def union(self, setB):
        setC = SetSorted()
        i, j = 0, 0
        while i < self.size() and j < setB.size():
            a, b = self.items[i], setB.items[j]
            if a == b:
                setC.insert(a)
                i += 1
                j += 1
            elif a < b:
                setC.insert(a)
                i += 1
            else:
                setC.insert(b)
                j += 1

        while i < self.size():
            setC.insert(self.items[i])
            i += 1

        while j < setB.size():
            setC.insert(setB.items[j])
            j += 1

        return setC

    def intersect(self, setB):
        setC = SetSorted()
        i, j = 0, 0
        while i < self.size() and j < setB.size():
            a, b = self.items[i], setB.items[j]
            if a == b:
                setC.insert(a)
                i += 1
                j += 1
            elif a < b:
                i += 1
            else:
                j += 1
        return setC

    def difference(self, setB):
        setC = SetSorted()
        i, j = 0, 0
        while i < self.size() and j < setB.size():
            a, b = self.items[i], setB.items[j]
            if a == b:
                i += 1
                j += 1
            elif a < b:
                setC.insert(a)
                i += 1
            else:
                j += 1
        while i < self.size():
            setC.insert(self.items[i])
            i += 1
        return setC