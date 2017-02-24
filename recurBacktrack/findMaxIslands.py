'''
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
