'''
Method 1 (Simple Solution) 
A Simple Solution is to sort the given array using a O(nlogn) sorting algorithm like Merge Sort, Heap Sort, etc and return the element at index k-1 in the sorted array. Time Complexity of this solution is O(nLogn).
'''
def kthSmallest(theSeq, k):

    # Sort the sequence
    theSeq = sorted(theSeq)

    # Print the kth element
    print theSeq[k-1]

'''
7
3
'''
if __name__ == "__main__":

    for theSeq in [[12, 3, 5, 7, 19], [1,2,3,4,5]]:
        kthSmallest(theSeq, 3)

        #! coding=utf-8

'''
Method 2 (Using Min Heap HeapSelect)
We can find kth smallest element in time complexity better than O(nLogn).
A simple optomization is to create a Min Heap of the given n elements and call extractMin() k times.
'''
class MinHeap:
    def __init__(self, aList, size):
        self.harr = aList
        self.capacity = size
        self.heap_size = size

        i = (self.heap_size -1) // 2
        while i >= 0:
            self.MinHeapify(i)
            i -= 1

    def parent(self, i):
        return (i-1) // 2

    def left(self, i):
        return (2*i + 1)

    def right(self, i):
        return 2*i+2

    def getMin(self):
        return self.harr[0]

    # remove minimum element (or root) from min heap
    def extractMin(self):
        if self.heap_size == 0:
            return -1

        # Store the mimimum value
        root = self.harr[0]

        # If there are more than 1 items, move the last item to root
        # and call heapify
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size-1]
            self.MinHeapify(0)

        self.heap_size -= 1

        return root

    # A recursive method to heapify a subtree with root at given index
    # This method assumes that the subtrees are already heapified
    def MinHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.heap_size and self.harr[l] < self.harr[i]:
            smallest = l
        if r < self.heap_size and self.harr[r] < self.harr[smallest]:
            smallest = r

        if smallest != i:
            self.harr[i],self.harr[smallest] = self.harr[smallest],self.harr[i]
            self.MinHeapify(smallest)

# kth Smallest element in a given array
def kthSmallest(arr, k):

    # Build a heap of n elements
    mh = MinHeap(arr, len(arr))

    # Do extract min (k-1) times
    for _ in range(0, k-1):
        mh.extractMin()

    # Return root
    return mh.getMin()

'''
5
7
10
'''
if __name__ == "__main__":
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 2
    print kthSmallest(arr, k)    
    
    arr = [7, 10, 4, 3, 20, 15]
    n = len(arr)
    k = 3
    print kthSmallest(arr, k)  
    
    arr = [7, 10, 4, 3, 20, 15]
    n = len(arr)
    k = 4
    print kthSmallest(arr, k)   
    
# This function returns kth smallest element in distinct arr[l..r]
# using quickSort based method,
# Assumption: elements in arr[] are distinct
def kthSmallest(arr, l, r, k):

    import random

    # standard partion process of quickSort
    # it considers the last element as pivot
    # and moves all smaller element to left of it and
    # greater elements to right, 
    # the function is used by randomPartition()
    def partition(arr, l, r):
        x = arr[r]
        i = l

        for j in range(l, r):
            if arr[j] <= x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i],arr[r] = arr[r], arr[i]
        return i

    # Picks a random pivot element between l and r and partitions
    # arr[l..r] arount the randomly picked element using partition
    def randomPartition(arr, l, r):
        n = r - l + 1
        pivot = random.randrange(n)
        arr[l+pivot],arr[r] = arr[r],arr[l+pivot]
        return partition(arr, l, r) 

    # If k is smaller than number of elements in array
    if k > 0 and k <= r - l + 1:
        # Partion the array around a random element and
        # get position of pivot element in sorted array
        pos = randomPartition(arr, l, r)

        # If position is the same as k
        if pos-l == k-1:
            return arr[pos]

        # If position is more, recur for left subarray
        if pos-l > k-1:
            return kthSmallest(arr, l, pos-1, k)

        # Else recur for right subarray
        return kthSmallest(arr, pos+1, r, k-pos+l-1)

    return -1

'''
7
10
5
'''
if __name__ == "__main__":
    for arr,k in [[[7, 10, 4, 3, 20, 15], 3], [[7, 10, 4, 3, 20, 15], 4], [[12, 3, 5, 7, 4, 19, 26], 3]]:
        print kthSmallest(arr, 0, len(arr)-1, k)
