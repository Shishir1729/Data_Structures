# Implement Union Find

class Node_Union_Find:
    def __init__(self, data = None):
        self.data = data
        self.parent = self
        self.rank = 0

class Union_Find:
    def __init__(self):
        self.sets = []

    def Make_Set(self, data):
        x = Node_Union_Find(data)
        self.sets.append(x)

    def Find_Set(self, x):
        if x != x.parent:
            x.parent = self.Find_Set(x.parent)
        return x.parent
    
    def Union(self, x, y):
        self.Link(self.Find_Set(x), self.Find_Set(y))
    
    def Link(self, x, y):
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y

            if x.rank == y.rank:
                y.rank += 1
    

