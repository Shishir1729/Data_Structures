# Implement a class for Doubly Linked Lists

class Node_Double:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        else:
            answer = ""
            current = self.head
            while current != None:
                answer += str(current.data) + "<->"
                current = current.next
            return answer[:-3]
    
    def add(self, item):
        temp = Node_Double(item)
        temp.next = self.head
        if self.head != None:
            self.head.prev = temp
        self.head = temp
    
    def search(self, item):
        if self.isEmpty():
            return False
        else:
            current = self.head
            found = False
            while not found and current != None:
                if current.data == item:
                    found = True
                else:
                    current = current.next
            if found:
                return current
            else:
                return False
    
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count
    
    def append(self, item):
        temp = Node_Double(item)
        if self.isEmpty():
            self.head = temp
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = temp
            temp.prev = current
    
    def insert(self, pos, item, size = None):
        if size == None:
            size = self.size()
        if pos == 0:
            self.add(item)
        elif pos == size:
            self.append(item)
        elif pos > size:
            raise Exception("Index out of range")
        else:
            temp = Node_Double(item)
            current = self.head
            count = 0
            while count < pos - 1:
                current = current.next
                count += 1
            temp.next = current.next
            current.next.prev = temp
            current.next = temp
            temp.prev = current

    def remove(self, item):
        answer = self.search(item)
        if not answer:
            raise Exception("Item not found")
        elif answer == self.head:
            self.head = self.head.next
            self.head.prev = None
        elif answer.next == None:
            answer.prev.next = None
        else:
            answer.prev.next = answer.next
            answer.next.prev = answer.prev

    def index(self, item):
        if not self.search(item):
            return -1
        
        count = 0
        current = self.head
        while current.data != item:
            count += 1
            current = current.next
        return count
    
    def Value(self, pos, size = None):
        if size == None:
            size = self.size()
        if pos >= size:
            raise Exception("Index out of range")
        else:
            current = self.head
            count = 0
            while count < pos:
                current = current.next
                count += 1
            return current
        
    
