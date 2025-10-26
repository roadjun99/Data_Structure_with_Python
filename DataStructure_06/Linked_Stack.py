class Node:
    def __init__(self,elem,link=None):
        self.data=elem
        self.link=link

class LinkedStack:
    def __init__(self):
        self.top=None

    def isEmpty(self): return self.top==None

    def isFull(self): return False

    def push(self,e):
        self.top=Node(e,self.top)

    def pop(self):
        if not self.isEmpty():
            n=self.top
            self.top=n.link
            return n.data

    def peek(self):
        if not self.isEmpty():
            return self.top.data
