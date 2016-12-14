'''
Minimum Cost Path with Left, Right, Bottom and Up moves allowed
Given a two dimensional grid, each cell of which contains integer cost which represents a cost to
traverse through that cell, we need to find a path from top left cell to bottom right cell by which 
total cost incurred is minimum.

Note : It is assumed that negative cost cycles do not exist in input matrix.

This problem is extension of below problem.

Min Cost Path with right and bottom moves allowed.

In previous problem only going right and bottom was allowed but in this problem we are allowed to go
bottom, up, right and left i.e. in all 4 direction.
'''

ROW = 5
COL = 5

import sys 

class Set:
    # Init
    def __init__(self):
        self._theElements = list()

    # Len
    def __len__(self):
        return len(self._theElements)

    # get 
    def __getitem__(self, index):
        return self._theElements[index]
    
    # isEmpty
    def isEmpty(self):
        return len(self) == 0

    # Equal
    def __equal__(self, setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf(setB)

    # is subset
    def isSubsetOf(self, setB):

        for item in self:
            if item not in setB:
                return False
        return True

    # add
    def insert(self, item):
        if item not in self:
            self._theElements.append(item)

    # remove
    def delete(self, item):
        assert item in self, "item must be in the set."
        self._theElements.remove(item)

    # union
    def union(self, setB):

        newSet = Set()
        newSet._theElements.extend(self)

        for item in setB:
            if item not in self:
                newSet._theElements.append(item)

        return newSet

    # intersection
    def interset(self, setB):

        newSet = Set()

        for item in setB:
            if item in self:
                newSet._theElements.append(item)

        return newSet

    # difference
    def difference(self, setB):

        newSet = Set()

        for item in self:
            if item not in setB:
                newSet._theElements.append(item)

        return newSet

    # find
    def find(self, entry):
        for item in self:
            if item == entry:
                return item

        return -1
    # iter
    def __iter__(self):
        return _MySetIterator(self._theElements)

# Iterator
class _MySetIterator:
    # Init
    def __init__(self, theElements):
        self._theElements = theElements
        self._index = 0
    def __iter__(self):
        return self
    def next(self):
        if self._index < len(self._theElements):
            item = self._theElements[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        

class Cell:
    # init
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

    # utility method for comparing two cells
    def __lt__(self, otherCell):
        if self.distance == otherCell.distance:
            if self.x != otherCell.x:
                return self.x < otherCell.x
            else:
                return self.y < otherCell.y

        return self.distance < otherCell.distance

# Utility method to check whether a point is 
# inside the grid or not
def isInsideGrid(i, j):

    return i >= 0 and i < COL and j >= 0 and j< ROW

# Method returns minimum cost to reach bottom
# right from top left
def shortest(grid, row, col):

    # initialize distance array by INT_MAX
    dis = [[None]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            dis[i][j] = sys.maxint

    # direction arrays for simplification of getting neighbour
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0,  -1]


    # init set
    st = Set()

    # insert (0, 0) cell with 0 distance
    st.insert(Cell(0, 0, 0))

    # initialize distance of (0, 0) with its grid value
    dis[0][0] = grid[0][0]

    # loop for standard dijkstra's algorithm
    while not st.isEmpty():
        # get the cell with minimum distance and delete it from the set
        k = st[0]
        st.delete(st[0])

        # loop through all neighbours
        for i in range(4):
            x = k.x + dx[i]
            y = k.y + dy[i]

            # if not inside boundry, ignore them
            if not isInsideGrid(x, y):
                continue

            # If distance from current cell is smaller, 
            # then update distance of neighbour cell
            if dis[x][y] > dis[k.x][k.y] + grid[x][y]:
                # If cell is already there in set, then
                # remove its previous entry
                if dis[x][y] != sys.maxint:
                    if st.find(Cell(x, y, dis[x][y])) != -1:
                        st.delete(Cell(x, y, dis[x][y]))

                # update the distance and insert new updatded
                # cell in set
                dis[x][y] = dis[k.x][k.y] + grid[x][y]
                st.insert(Cell(x, y, dis[x][y]))

    # dis[row-1][col-1] will represent final
    # distance of bottom right cell from top left cell
    return dis[row-1][col-1]

'''
327
'''
if __name__ == "__main__":
    grid = [[31, 100, 65, 12, 18],
            [10, 13, 47, 157, 6],
            [100, 113, 174, 11, 33],
            [88, 124, 41, 20, 140],
            [99, 32, 111, 41, 20]]

    print shortest(grid, ROW, COL)
