#Implement a class for Circular Doubly Linked Lists
from Doubly_Linked_Lists import DoublyLinkedList, Node_Double

class CircularDoublyLinkedList(DoublyLinkedList):
    def __init__(self):
        self.head = None
        self.size = 0
        
    def isEmpty(self):
        return DoublyLinkedList.isEmpty(self)
    
    def __str__(self):
        return DoublyLinkedList.__str__(self) + "<->" + str(self.head.data)
    
    def add(self, item):
        temp = Node_Double(item)
        if self.isEmpty():
            temp.next = temp
            temp.prev = temp
            self.head = temp
        else:
            temp.next = self.head
            temp.prev = self.head.prev
            self.head.prev.next = temp
            self.head.prev = temp
            self.head = temp
        self.size += 1
        
    def search(self, item):
        pos = 0
        current = self.head
        found = False
        while not found and pos < self.size:
            if current.data == item:
                found = True
            else:
                current = current.next
                pos += 1
        if found:
            return current
        else:
            return False
        
    def size(self):
        return self.size
    
    def insert(self, pos, item):
        super().insert(pos, item, self.size)
        self.size += 1

    def remove(self, item):
        answer = self.search(item)
        if not answer:
            raise Exception("Item not found")
        
        if self.size == 1:
            self.head = None
            self.size -= 1

        else:
            if answer == self.head:
                self.head = self.head.next
            answer.prev.next = answer.next
            answer.next.prev = answer.prev
            self.size -= 1

    def index(self, item):
        if not self.search(item):
            return -1
        
        pos = 0
        current = self.head
        while current.data != item:
            current = current.next
            pos += 1
        return pos
    
    def Value(self, pos):
        return super().Value(pos, self.size)
    


    

