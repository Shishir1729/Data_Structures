#Implement Binary Trees with parent pointers

class Node_Binary_Tree_P:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree_P:
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
                    
    def delete(self, data):
        answer = self.search(data)

        if not answer:
            raise ValueError("Data not found")
        
        if answer == answer.parent.left:
            if answer.left == None:
                if answer.right == None:
                    answer.parent.left = None
            
                else:
                    answer.parent.left = answer.right
                    answer.right.parent = answer.parent
            else:
                if answer.right == None:
                    answer.parent.left = answer.left
                    answer.left.parent = answer.parent
                else:
                    answer.parent.left = answer.left
                    answer.left.parent = answer.parent
                    x = answer.right
                    y = answer.left
                    while y.left != None:
                        y = y.left
                    y.left = x

        else:
            if answer.left == None:
                if answer.right == None:
                    answer.parent.right = None
            
                else:
                    answer.parent.right = answer.right
                    answer.right.parent = answer.parent
            else:
                if answer.right == None:
                    answer.parent.right = answer.left
                    answer.left.parent = answer.parent
                else:
                    answer.parent.right = answer.left
                    answer.left.parent = answer.parent
                    x = answer.right
                    y = answer.left
                    while y.left != None:
                        y = y.left
                    y.left = x

    def insert(self, data):
        if self.isEmpty():
            self.root = Node_Binary_Tree_P(data)
        else:
            if self.search(data):
                raise ValueError("Data already in tree")
            
            x = self.root

            while x.left != None and x.right != None:
                x = x.left
            if x.left == None:
                x.left = Node_Binary_Tree_P(data)
                x.left.parent = x
            else:
                x.right = Node_Binary_Tree_P(data)
                x.right.parent = x
            
