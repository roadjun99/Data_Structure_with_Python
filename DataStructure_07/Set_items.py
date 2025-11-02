class itemsSet:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def contains(self, item):
        for i in range(self.size):
            if self.items[i] == item:
                return True
        return False

    def insert(self, item):
        if not self.contains(item):
            self.items.append(item)
            self.size += 1

    def delete(self, item):
        if not self.contains(item):
            return
        self.items.remove(item)

    def display(self, msg):
        print(msg, self.items)

    def __eq__(self, setB):
        if self.size != setB.size:
            return False
        for i in range(self.size):
            if self.items[i] != setB.items[i]:
                return False
        return True

    def union(self, setB):
        setC = itemsSet()
        for i in range(self.size):
            setC.insert(self.items[i])
        for i in range(setB.size):
            if not setC.contains(setB.items[i]):
                setC.insert(setB.items[i])
        return setC

    def intersect(self, setB):
        setC = itemsSet()
        for i in range(self.size):
            if setB.contains(self.items[i]):
                setC.insert(self.items[i])
        return setC

    def difference(self, setB):
        setC = itemsSet()
        for i in range(self.size):
            if not setB.contains(self.items[i]):
                setC.insert(self.items[i])
        return setC