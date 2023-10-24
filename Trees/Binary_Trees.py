# Implement Binary Trees 

class Node_Binary_Tree:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def search(self, data):
        if self.isEmpty():
            return False
        else:
            if self.root.data == data:
                return True
            else:
                answer1 = self.search(self.root.left, data)
                answer2 = self.search(self.root.right, data)
                if not answer1 and not answer2:
                    return False
                else:
                    if answer1:
                        return answer1
                    else:
                        return answer2
                    
    def insert(self, data):
        if self.isEmpty():
            self.root = Node_Binary_Tree(data)
        else:
            if self.search(data):
                raise ValueError("Data already in tree")
            
            x = self.root

            while x.left != None and x.right != None:
                x = x.left

            if x.left == None:
                x.left = Node_Binary_Tree(data)
            else:
                x.right = Node_Binary_Tree(data)
    
    def delete(data):
        pass
        

    

    
