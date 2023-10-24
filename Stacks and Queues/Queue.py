#Implement a class for Queue
import math

class Queue:
    def __init__(self, size = math.inf):
        self.head = 0
        self.tail = 0
        self.size = size
        if size == math.inf:
            self.items = []
        else:
            self.items = [None] * size
        
    def isEmpty(self):
        return self.head == self.tail
    
    def enqueue(self,item):
        if self.size == math.inf:
            self.items.append(item)
            self.tail += 1
        else:
            if self.tail == self.size:
                if self.head == 0:
                    raise Exception("Queue is full")
                else:
                    self.items[0] = item
                    self.tail = 1
            else:
                if self.tail + 1 == self.head:
                    raise Exception("Queue is full")
                else:
                    self.items[self.tail] = item
                    self.tail += 1
            
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        elif self.size == math.inf:
            self.tail -= 1
            return self.items.pop(0)
        else:
            answer = self.items[self.head]
            self.items[self.head] = None
            self.head += 1
            if self.head == self.size:
                self.head = 0
            return answer
        
    def size(self):
        return self.size
    
    def __str__(self):
        return str(self.items)
