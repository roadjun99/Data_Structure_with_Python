from Linked_Stack import Node

class LinkedQueue:
    def __init__(self):
        self.tail=None

    def isEmpty(self): return self.tail==None
    def isFull(self): return False

    def enqueue(self,item):
        node=Node(item,None)
        if self.isEmpty():
            self.tail=node
            node.link=node
        else:
            node.link=self.tail.link
            self.tail.link=node
            self.tail=node

    def dequeue(self):
        if not self.isEmpty():
            data=self.tail.link.data
            if self.tail.link==self.tail:
                self.tail=None
            else:
                self.tail.link=self.tail.link.link
            return data