'''
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.
In every iteration of selection sort, the minimum element (considering ascending order) from
the unsorted subarray is picked and moved to the sorted subarray.

Time Complexity: O(n2) as there are two nested loops.
Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps
and can be useful when memory write is a costly operation.
'''
def selectSort(theSeq):

    n = len(theSeq)
    for i in range(n-1):
        smallNdx = i
        for j in range(i+1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j

        if smallNdx != i:
            tmp = theSeq[smallNdx]
            theSeq[smallNdx] = theSeq[i]
            theSeq[i] = tmp

'''
[-1, 2, 3, 5, 7]
'''
if __name__ == "__main__":
    theSeq = [2, -1, 3, 5, 7]
    selectSort(theSeq)
    print theSeq
