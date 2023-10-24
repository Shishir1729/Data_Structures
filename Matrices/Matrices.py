
class Matrix:
    def __init__(self, rows, cols, data):
        self.rows = rows
        self.cols = cols
        self.data = [[data[j][i] for i in range(cols)] for j in range(rows)]
    
    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise Exception("Matrices must be the same size to add")
        else:
            return Matrix(self.rows, self.cols, [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])
        
    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise Exception("Matrices must be the same size to subtract")
        else:
            return Matrix(self.rows, self.cols, [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])
        
    def __mul__(self, other):
        if self.cols != other.rows:
            raise Exception("Matrices must be compatible to multiply")
        else:
            return Matrix(self.rows, other.cols, [[sum([self.data[i][k] * other.data[k][j] for k in range(self.cols)]) for j in range(other.cols)] for i in range(self.rows)])
    
    def __rmul__(self, other):
        return Matrix(self.rows, self.cols, [[other * self.data[i][j] for j in range(self.cols)] for i in range(self.rows)])
    
    def __str__(self):
        return str(self.data)
    

class Vector:
    def __init__(self, dimension, data):
        self.dimension = dimension
        if len(data) != dimension:
            raise Exception("Vector must be of the correct dimension")
        self.data = data
    
    def __add__(self, other):
        if self.dimension != other.dimension:
            raise Exception("Vectors must be the same size to add")
        else:
            return Vector(self.dimension, [self.data[i] + other.data[i] for i in range(self.dimension)])
    
    def __sub__(self, other):
        if self.dimension != other.dimension:
            raise Exception("Vectors must be the same size to subtract")
        else:
            return Vector(self.dimension, [self.data[i] - other.data[i] for i in range(self.dimension)])
        
    def __mul__(self, other):
        if self.dimension != other.dimension:
            raise Exception("Vectors must be the same size to multiply")
        else:
            return sum([self.data[i] * other.data[i] for i in range(self.dimension)])
        
    def __rmul__(self, other):
        return Vector(self.dimension, [other * self.data[i] for i in range(self.dimension)])