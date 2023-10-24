# Implement a class for Stack
import math

class Stack:
    def __init__(self, size = math.inf):
        self.top = -1
        self.size = size
        if size == math.inf:
            self.items = []
        else:
            self.items = [None] * size
    
    def isEmpty(self):
        return self.top == -1
    
    def push(self,item):
        if self.size == math.inf:
            self.items.append(item)
            self.top += 1
        else:
            if self.top + 1 == self.size:
                raise Exception("Stack is full")
            else:
                self.top += 1
                self.items[self.top] = item
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        elif self.size == math.inf:
            self.top -= 1
            return self.items.pop()
        else:
            answer = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return answer
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[self.top]
    
    def size(self):
        return self.size
    
    def __str__(self):
        return str(self.items)