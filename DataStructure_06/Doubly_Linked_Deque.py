class DNode:
    def __init__ (self, elem, prev, next):
        self.data = elem
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__( self ):
        self.front = None
        self.rear = None

    def isEmpty( self ): return self.front == None
    def isFull( self ): return False

    def addFront( self, item ):
        node = DNode(item, None, self.front)
        if( self.isEmpty()):
            self.front = self.rear = node
        else :
            self.front.prev = node
            self.front = node

    def addRear( self, item ):
        node = DNode(item, self.rear, None)
        if( self.isEmpty()):
            self.front = self.rear = node
        else :
            self.rear.next = node
            self.rear = node

    def deleteFront( self ):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front==None :
                self.rear = None
            else:
                self.front.prev = None
            return data

    def deleteRear( self ):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear==None :
                self.front = None
            else:
                self.rear.next = None
            return data

    def __str__( self ) :
        arr = []
        node = self.front
        while not node == None :
            arr.append(node.data)
            node = node.next
        return str(arr)