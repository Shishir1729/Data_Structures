import sys
sys.path.insert(0, '../Linked Lists')
from Singly_Linked_Lists import SinglyLinkedList, Node_Single

class Undirected_Graph:
    def __init__(self):
        self.vertices = 0
        self.adjacency_list = []

    def add_vertex(self):
        self.vertices += 1
        self.adjacency_list.append(SinglyLinkedList())

    def add_edge(self, src, dest):
        self.adjacency_list[src].add(dest)
        self.adjacency_list[dest].add(src)

    def print_graph(self):
        for i in range(self.vertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            str(self.adjacency_list[i])

    def degree(self, vertex):
        return self.adjacency_list[vertex].size()
    
    def isEdge(self, src, dest):
        return True if self.adjacency_list[src].search(dest) else False
    
    def delete_edge(self, src, dest):
        self.adjacency_list[src].remove(dest)
        self.adjacency_list[dest].remove(src)

    def delete_vertex(self, vertex):
        if self.vertices == 0:
            raise ValueError("The graph is empty")
        if vertex >= self.vertices:
            raise IndexError("The vertex does not exist")
        # Delete the vertex from all the adjacency lists
        for i in range(self.vertices):
            if self.isEdge(i, vertex):
                self.delete_edge(i, vertex)
        # Delete the vertex from the adjacency list
        self.adjacency_list.pop(vertex)
        self.vertices -= 1


class Directed_Graph:
    def __init__(self):
        self.vertices = 0
        self.adjacency_list = []

    def add_vertex(self):
        self.vertices += 1
        self.adjacency_list.append(SinglyLinkedList())

    def add_edge(self, src, dest):
        self.adjacency_list[src].add(dest)

    def print_graph(self):
        for i in range(self.vertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            str(self.adjacency_list[i])

    def outdegree(self, vertex):
        return self.adjacency_list[vertex].size()
    
    def indegree(self, vertex):
        count = 0
        for i in range(self.vertices):
            if self.isEdge(i, vertex):
                count += 1
        return count
    
    def isEdge(self, src, dest):
        return True if self.adjacency_list[src].search(dest) else False
    
    def delete_edge(self, src, dest):
        self.adjacency_list[src].remove(dest)

    def delete_vertex(self, vertex):
        if self.vertices == 0:
            raise ValueError("The graph is empty")
        
        if vertex >= self.vertices:
            raise IndexError("The vertex does not exist")
        
        # Delete the vertex from all the adjacency lists
        for i in range(self.vertices):
            if self.isEdge(i, vertex):
                self.delete_edge(i, vertex)

        # Delete the vertex from the adjacency list
        self.adjacency_list.pop(vertex)
        self.vertices -= 1 


