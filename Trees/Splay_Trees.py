#Implement Splay Trees

class Node_Splay_Tree():
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.parent = None

class Splay_Tree():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None
    
    def search(self, key):
        if self.isEmpty():
            return False
        
        
        node = self.root

        while node != None:
            if node.data == key:
                self.splay(self.root)
                return self.root
            elif node.data > key:
                if self.root.left == None:
                    return False
                else:
                    node = node.left
            else:
                if self.root.right == None:
                    return False
                else:
                    node = node.right
        return False   
        
    def splay(self):
        while self.root.parent != None:    
            if self.root.parent.parent == None:
                if self.root.parent.left == self.root:
                    self.rotate_right(self.root.parent)
                else:
                    self.rotate_left(self.root.parent)
            
            else:
                if self.root.parent.left == self.root:
                    if self.root.parent.parent.left == self.root.parent:
                        self.rotate_right(self.root.parent.parent)
                        self.rotate_right(self.root.parent)
                    
                    else:
                        self.rotate_right(self.root.parent)
                        self.rotate_left(self.root.parent)
                
                else:
                    if self.root.parent.parent.right == self.root.parent:
                        self.rotate_left(self.root.parent.parent)
                        self.rotate_left(self.root.parent)
                    
                    else:
                        self.rotate_left(self.root.parent)
                        self.rotate_right(self.root.parent)
        
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def rotate_right(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def insert(self, key):
        if self.isEmpty():
            self.root = Node_Splay_Tree(key)
        elif self.search(key) != False:
            raise ValueError("Data already in tree")
        else:
            node = self.root
            while node != None:
                if node.data > key:
                    if node.left == None:
                        node.left = Node_Splay_Tree(key)
                        node.left.parent = node
                        self.splay(node.left)
                        return
                    else:
                        node = node.left
                else:
                    if node.right == None:
                        node.right = Node_Splay_Tree(key)
                        node.right.parent = node
                        self.splay(node.right)
                        return
                    else:
                        node = node.right

    def delete(self, key):
        if self.isEmpty():
            raise ValueError("Tree is empty")
        
        node = self.search(key)
        if node == False:
            raise ValueError("Data not found")
        
        if node.left == None:
            if node.right == None:
                if node == self.root:
                    self.root = None
                else:
                    if node.parent.left == node:
                        node.parent.left = None
                    else:
                        node.parent.right = None
                
                return
            
            else:
                if node == self.root:
                    self.root = node.right
                    node.right.parent = None
                else:
                    if node.parent.left == node:
                        node.parent.left = node.right
                        node.right.parent = node.parent
                    else:
                        node.parent.right = node.right
                        node.right.parent = node.parent
                
                return
            
        else:
            if node.right == None:
                if node == self.root:
                    self.root = node.left
                    node.left.parent = None
                else:
                    if node.parent.left == node:
                        node.parent.left = node.left
                        node.left.parent = node.parent
                    else:
                        node.parent.right = node.left
                        node.left.parent = node.parent
                
                return
            
            else:
                x = node.right
                while x.left != None:
                    x = x.left
                
                if x.parent.left == x:
                    x.parent.left = x.right
                    if x.right != None:
                        x.right.parent = x.parent
                else:
                    x.parent.right = x.right
                    if x.right != None:
                        x.right.parent = x.parent
                
                node.data = x.data
                return
    
        