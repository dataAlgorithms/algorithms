'''
Method One:

For a given matrix the elements can be 1s or 0s . 
The filled cells that are connected form a region. 
Two cells are said to be connected if they are connected 
if they are adjacent to each other horizontally, vertically or
 diagonally . There may be several regions in the matrix.
  How do you find the largest region (in terms of number of cells)
   in the matrix ?
'''
def getval(A, i, j, L, H):

    if i < 0 or i >= L or j < 0 or j >=H:
        return 0
    else:
        return A[i][j]

def findMaxBlock(A, r, c, L, H, size, cntarr, maxsize):

    if r >= L or c >= H:
        return

    cntarr[r][c] = True
    size += 1

    if size > maxsize:
        maxsize = size

    # search in eight directions
    direction = [[-1, 0],
                 [-1, -1],
                 [0, -1],
                 [1, -1],
                 [1, 0],
                 [1, 1],
                 [0, 1], 
                 [-1, 1]]

    for i in range(8):
        newi = r + direction[i][0]
        newj = c + direction[i][1]
        val = getval(A, newi, newj, L, H)
        if val > 0 and cntarr[newi][newj] is False:
            maxsize = findMaxBlock(A, newi, newj, L, H, size, cntarr, maxsize)
            
    cntarr[r][c] = False
    
    return maxsize


def getMaxOnes(A, rmax, colmax):

    maxsize = 0
    size = 0
    cntarr = [[False]* colmax for _ in range(rmax)]
    for i in range(rmax):
        for j in range(colmax):
            if A[i][j] == 1:
                maxsize = findMaxBlock(A, i, j, rmax, colmax, 0, cntarr, maxsize)

    return maxsize

'''
5
11
'''
if __name__ == "__main__":
    zarr = [[1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1]]
    print getMaxOnes(zarr, 5, 5)

    zarr = [[1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1],
            [0, 0, 0, 1, 1],
            [1, 0, 0, 1, 1],
            [0, 1, 0, 1, 1]]
    print getMaxOnes(zarr, 5, 5)

    
'''
Method two:
'''
# Program to count islands in boolean 2D matrix
class Graph:
 
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
 
    # A function to check if a given cell 
    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1 
        # and not yet visited
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j])
             
 
    # A utility function to do DFS for a 2D 
    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited, length):
 
        # These arrays are used to get row and 
        # column numbers of 8 neighbours 
        # of a given cell
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1];
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1];
         
        # Mark this cell as visited
        visited[i][j] = True
 
        # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
               length += 1 
               length = self.DFS(i + rowNbr[k], j + colNbr[k], visited, length)
 
        return length

    # The main function that returns
    # count of islands in a given boolean
    # 2D matrix
    def maxIsland(self):
        # Make a bool array to mark visited cells.
        # Initially all cells are unvisited
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]
 
        # Initialize count as 0 and travese 
        # through the all cells of
        # given matrix
        maxLength = 0
        length = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                # If a cell with value 1 is not visited yet, 
                # then new island found
                if visited[i][j] == False and self.graph[i][j] ==1:
                    # Visit all cells in this island 
                    # and increment island count
                    length = 1
                    length = self.DFS(i, j, visited, length)
                    if length > maxLength:
                        maxLength = length
 
        return maxLength
'''
Max islands is :
4
Max islands is :
6
'''
if __name__ == "__main__": 
    graph = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]
 
    row = len(graph)
    col = len(graph[0])
 
    g = Graph(row, col, graph)
 
    print "Max islands is :"
    print g.maxIsland()

    graph = [[0, 0, 1, 1, 0],
            [1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1]]
 
    row = len(graph)
    col = len(graph[0])
 
    g = Graph(row, col, graph)
 
    print "Max islands is :"
    print g.maxIsland()
