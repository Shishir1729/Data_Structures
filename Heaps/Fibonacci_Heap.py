#Implement Fibonacci Heaps
import math

class Node_Fibonacci_Heap:
    def __init__(self, data = None):
        self.data = data
        self.degree = 0
        self.parent = None
        self.leftmost_child = None
        self.left = None
        self.right = None
        self.mark = False

class Fibonacci_Heap:
    def __init__(self):
        self.min = None
        self.n = 0

    def Fib_Heap_Insert(self, data):
        x = Node_Fibonacci_Heap(data)
        if self.min == None:
            self.min = x
            x.left = x
            x.right = x
        else:
            x.left = self.min
            x.right = self.min.right
            self.min.right = x
            x.right.left = x
            if x.data < self.min.data:
                self.min = x
        self.n += 1

    def Find_Min(self):
        return self.min.data
    
    def Fib_Heap_Union(self, H2):
        H = Fibonacci_Heap()
        H.min = self.min
        H.min.right.left = H2.min.left
        H2.min.left.right = H.min.right
        H.min.right = H2.min
        H2.min.left = H.min
        if H.min == None or (H2.min != None and H2.min.data < H.min.data):
            H.min = H2.min
        H.n = self.n + H2.n
        return H
    
    def Fib_Heap_Extract_Min(self):
        z = self.min   
        if z != None:
            if z.leftmost_child != None:
                x = z.leftmost_child
                while x.right != z.leftmost_child:
                    x.parent = None
                    x = x.right
                x.parent = None
                x.right = z.right
                z.right.left = x
                z.left.right = z.leftmost_child
                z.leftmost_child.left = z.left
                z.leftmost_child = None
            else:
                z.right.left = z.left
                z.left.right = z.right

            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self.Consolidate()
            self.n -= 1
        return z

    def Consolidate(self):
        A = [None] * self.D(self.n)

        for i in range(0, self.D(self.n)):
            A[i] = None
        
        w = self.min
        length = self.root_length()

        while length > 0:
            x = w
            d = x.degree
            while A[d] != None:
                y = A[d]
                if x.data > y.data:
                    x, y = y, x
                self.Fib_Heap_Link(y, x)
                A[d] = None
                d += 1
            A[d] = x
            w = w.right
            length -= 1
        
        self.min = None
        
        for tree in A:
            if tree != None:
                if self.min == None:
                    self.min = tree
                    self.min.left = self.min
                    self.min.right = self.min
                else:
                    tree.left = self.min
                    tree.right = self.min.right
                    self.min.right = tree
                    tree.right.left = tree
                    if tree.data < self.min.data:
                        self.min = tree

    def D(self, n):
        return math.floor(math.log(n, 1.5))
    
    def Fib_Heap_Link(self, y, x):
        y.right.left = y.left
        y.left.right = y.right
        y.parent = x
        if x.leftmost_child == None:
            x.leftmost_child = y
            y.left = y
            y.right = y
        else:
            y.left = x.leftmost_child
            y.right = x.leftmost_child.right
            x.leftmost_child.right = y
            y.right.left = y
        x.degree += 1
        y.mark = False
    
    def root_length(self):
        if self.min == None:
            return 0
        else:
            x = self.min
            length = 1
            while x.right != self.min:
                length += 1
                x = x.right
            return length
        
    def Fib_Heap_Decrease_Key(self, x, k):
        if k > x.data:
            raise ValueError("New key is greater than current key")
        x.data = k
        y = x.parent
        if y != None and x.data < y.data:
            self.Cut(x, y)
            self.Cascading_Cut(y)
        if x.data < self.min.data:
            self.min = x

    def Cut(self, x, y):
        if x.right == x:
            y.leftmost_child = None
        else:
            x.right.left = x.left
            x.left.right = x.right
            if y.leftmost_child == x:
                y.leftmost_child = x.right
        y.degree -= 1
        x.parent = None
        x.right = self.min
        x.left = self.min.left
        self.min.left = x
        x.left.right = x
        x.mark = False

    def Cascading_Cut(self, y):
        z = y.parent
        if z != None:
            if y.mark == False:
                y.mark = True
            
            else:
                self.Cut(y, z)
                self.Cascading_Cut(z)
    
    def Fib_Heap_Delete(self, x):
        self.Fib_Heap_Decrease_Key(x, -math.inf)
        self.Fib_Heap_Extract_Min()
    
