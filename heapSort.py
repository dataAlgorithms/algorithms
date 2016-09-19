'''
1. heap sort
'''
def heapSort(arr):

    # To heapify subtree rooted at index i.
    # n is size of heap
    def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1     # left = 2*i + 1
        r = 2 * i + 2     # right = 2*i + 2
     
        # See if left child of root exists and is
        # greater than root
        if l < n and arr[i] < arr[l]:
            largest = l
     
        # See if right child of root exists and is
        # greater than root
        if r < n and arr[largest] < arr[r]:
            largest = r
     
        # Change root, if needed
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]  # swap
     
            # Heapify the root.
            heapify(arr, n, largest)

    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
  
'''
[-30, -20, 0, 1, 10, 20, 50]
'''
if __name__ == "__main__":
    theSeq = [20, 10, 1, 0, -20, -30, 50]
    heapSort(theSeq)
    print theSeq
    
'''
2. Sort a nearly sorted (or K sorted) array
'''
class MinHeap:
    def __init__(self, harr, heap_size):

        self.harr = harr
        self.heap_size = heap_size
        
        i = (heap_size - 1) / 2
        while i >= 0:
            self.minHeapify(i)
            i -= 1

    # heapify a subtree with root at given index
    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.heap_size and self.harr[l] < self.harr[i]:
            smallest = l

        if r < self.heap_size and self.harr[r] < self.harr[smallest]:
            smallest = r

        if smallest != i:
            self.harr[i],self.harr[smallest] = self.harr[smallest],self.harr[i]
            self.minHeapify(smallest)

    # get the index of left child of node at index i
    def left(self, i):
        return 2*i + 1

    # get the index of right child of node at index i
    def right(self, i):
        return 2*i + 2

    # remove min (or root), add a new value x, and return old root
    def replaceMin(self, x):
        root = self.harr[0]
        self.harr[0] = x
        if root < x:
            self.minHeapify(0)
        return root

    # extract the root which is the minimum element
    def extractMin(self):
        root = self.harr[0]
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size-1]
            self.heap_size -= 1
            self.minHeapify(0)
        return root

# Given an array of size n, where every element is k away from its target
# position, sorts the array in O(nLogK)time
def sortK(arr, k):

    # get the length of arr
    n = len(arr)

    # Create a Min heap of first (k+1) elements from input array
    harr = [0] * (k+1)
    i = 0
    while True:
        if i > k or i >= n:
            break

        harr[i] = arr[i]
        i += 1

    hp = MinHeap(harr, k+1)

    # i is index for remaining elements in arr and
    # ti is target index of for currement minimum element in Min heapm hp
    i = k+1
    for ti  in range(0, n):
        if i < n:
            arr[ti] = hp.replaceMin(arr[i])
        else:
            arr[ti] = hp.extractMin()

        i += 1

'''
[2, 3, 6, 8, 12, 56]
'''
if __name__ == "__main__":
    k = 3
    arr = [2, 6, 3, 12, 56, 8]
    sortK(arr, k)

    print arr
