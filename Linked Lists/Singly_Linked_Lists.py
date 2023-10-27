# Implement a Class for Singly Linked Lists

class Node_Single:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def __str__(self):
        if self.isEmpty():
            return ""
        else:
            answer = ""
            current = self.head
            while current != None:
                answer += str(current.data) + "->"
                current = current.next
            return answer[:-2]
    
    def add(self, item):
        temp = Node_Single(item)
        temp.next = self.head
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
        temp = Node_Single(item)
        if self.isEmpty():
            self.head = temp
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = temp
    
    def index(self, item):
        if not self.search(item):
            return -1

        count = 0
        current = self.head
        while current.data != item:
            count += 1
            current = current.next
        return count
    
    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        elif pos == self.size():
            self.append(item)
        elif pos > self.size():
            raise Exception("Index out of range")
        else:
            temp = Node_Single(item)
            current = self.head
            for i in range(pos - 1):
                current = current.next
            temp.next = current.next
            current.next = temp
    
    def delete(self, item):
        if not self.search(item):
            raise Exception("Item not found")
        
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next

    def Value(self, pos):
        if pos >= self.size():
            raise Exception("Index out of range")
        
        current = self.head
        for i in range(pos):
            current = current.next
        return current.data
    

        



        

        