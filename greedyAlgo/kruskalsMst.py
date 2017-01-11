# Kruska's algorithm to find Minimum Spanning Tree
# of a given connected, undirected and weighted graph
'''
Time Complexity: O(ElogE) or O(ElogV). Sorting of edges takes O(ELogE) time.
 After sorting, we iterate through all edges and apply find-union algorithm. 
 The find and union operations can take atmost O(LogV) time. So overall complexity 
 is O(ELogE + ELogV) time. The value of E can be atmost O(V2), so O(LogV) are O(LogE) same.
  Therefore, overall time complexity is O(ElogE) or O(ElogV)
'''
from collections import defaultdict

# class to represent a graph
class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])

    # A utility function to find set of an element i
    # uses path compression techinque
    def find(self, parent, i):
        if parent[i] == i:
            return i

        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # uses union by rank
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # If ranks are same, then make one as root and increment
        # its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Krukal's algorithm
    def KruskalMST(self):
    
        result = [] # this will store the resultant MST

        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]

        # Step1: Sort all the edges in non-decreasing order of their
        # weight, If we are not allowed to change the given graph, we
        # can create a copy of graph
        self.graph = sorted(self.graph,key=lambda item: item[2])

        parent = [];
        rank = []

        # Create v subsets with single elements
        for node in range(self.v):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to v-1
        while e < self.v - 1:

            # Step 2: Pick the smallest edge and increment the index
            # for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does not cause cycle, include it
            # in result and increment the index of reslt for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        # print the contents of result[] to display the built MST
        print "Following are the edges in the constructed MST"
        for u, v, weight in result:
            print "%d -- %d == %d" % (u, v, weight)

'''
Following are the edges in the constructed MST
2 -- 3 == 4
0 -- 3 == 5
0 -- 1 == 10
'''
if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)
    g.KruskalMST()
