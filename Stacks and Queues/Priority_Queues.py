#Implement Priority Queues using binary heaps and list data structure

class Binary_Heap():
    def __init__(self):
        self.heap = []
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def insert(self, key):
        self.heap.append(key)
        self.size += 1
        self.heapify_up(self.size-1)

    def heapify_up(self, index):
        while index > 0:
            parent = (index-1)//2
            if self.heap[parent] < self.heap[index]:
                self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                index = parent
            else:
                break

    def extract_min(self):
        if self.isEmpty():
            return False
        else:
            self.heap[0], self.heap[self.size-1] = self.heap[self.size-1], self.heap[0]
            self.size -= 1
            self.heapify_down(0)
            return self.heap.pop()

    def heapify_down(self, index):
        while index < self.size:
            left = 2*index + 1
            right = 2*index + 2
            if left < self.size and right < self.size:
                if self.heap[left] > self.heap[right]:
                    if self.heap[left] > self.heap[index]:
                        self.heap[left], self.heap[index] = self.heap[index], self.heap[left]
                        index = left
                    else:
                        break
                else:
                    if self.heap[right] > self.heap[index]:
                        self.heap[right], self.heap[index] = self.heap[index], self.heap[right]
                        index = right
                    else:
                        break
            elif left < self.size:
                if self.heap[left] > self.heap[index]:
                    self.heap[left], self.heap[index] = self.heap[index], self.heap[left]
                    index = left
                break
            else:
                break

    def delete(self, index):
        if index >= self.size:
            raise IndexError("Index out of range")
        
        self.heap[index], self.heap[self.size-1] = self.heap[self.size-1], self.heap[index]
        self.size -= 1
        self.heapify_down(index)
        return self.heap.pop()
    
    def __str__(self):
        return str(self.heap)
