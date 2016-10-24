'''
Method 1 (Simple Solution) 
A Simple Solution is to sort the given array using a O(nlogn) sorting algorithm like Merge Sort, 
Heap Sort, etc and return the element at index k-1 in the sorted array. Time Complexity of this solution is O(nLogn).
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
    
#! coding=utf-8

'''
Method 3 (Using Max-Heap)
We can also use Max Heap for finding the kth smallest element. Following is algorithm.
1) Build a Max-Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array. O(k)

2) For each element, after the kth element (arr[k] to arr[n-1]), compare it with root of MH.
a) If the element is less than the root then make it root and call heapify for MH
b) Else ignore it.
// The step 2 is O((n-k)*logk)

3) Finally, root of the MH is the kth smallest element.

Time complexity of this solution is O(k + (n-k)*Logk)
'''
class MaxHeap:
    def __init__(self, aList, size):
        self.harr = aList
        self.heap_size = size
        i = (self.heap_size-1) // 2
        while i >= 0:
            self.maxHeapify(i)
            i -= 1

    def parent(self, i):
        return (i-1) / 2

    def left(self,  i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2

    def getMax(self):
        return self.harr[0]

    def replaceMax(self, x):
        self.harr[0] = x
        self.maxHeapify(0)

    # remove maximum element (or root) from max heap
    def extractMax(self):
        if self.heap_size == 0:
            return -1

        # Store the maximum value
        root = self.harr[0]

        # If there are more than 1 items, move the last item
        # to root and call heapify
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size -1]
            self.maxHeapify(0)

        self.heap_size -= 1

        return root

    # A recursive method to heapify a subtree with root at given index
    # This method assumes that the subtrees are already heapified
    def maxHeapify(self,  i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.heap_size and self.harr[l] > self.harr[i]:
            largest = l
        if r < self.heap_size and self.harr[r] > self.harr[largest]:
            largest = r
        if largest != i:
            self.harr[i],self.harr[largest] = self.harr[largest],self.harr[i]
            self.maxHeapify(largest)

# Function to return kth largest element in a given array
def kthSmallest(arr, k):

    # Build a heap of first k elements: O(k) time
    mh = MaxHeap(arr, k)

    # Process remaining n-k elements, If current element is 
    # smaller than root, replace root with current element
    n = len(arr)
    for i in range(k, n):
        if arr[i] < mh.getMax():
            mh.replaceMax(arr[i])

    # Return root
    return mh.getMax()

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

    #! coding=utf-8

'''
Method 4 (QuickSelect) 
This is an optimization over method 1 if QuickSort is used as a sorting algorithm in first step. 
In QuickSort, we pick a pivot element, then move the pivot element to its correct position and 
partition the array around it. The idea is, not to do complete quicksort, but stop at the point 
where pivot itself is k’th smallest element. Also, not to recur for both left and right sides of
 pivot, but recur for one of them according to the position of pivot. The worst case time 
 complexity of this method is O(n2), but it works in O(n) on average.
'''
def kthSmallest(arr, l, r, k):

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

    # If k is smaller than number of elements in array
    if k > 0 and k <= r - l + 1:
        # Partion the array around a random element and
        # get position of pivot element in sorted array
        pos = partition(arr, l, r)

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
5
7
10
'''
if __name__ == "__main__":
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 2
    print kthSmallest(arr, 0, n-1, k)    
    
    arr = [7, 10, 4, 3, 20, 15]
    n = len(arr)
    k = 3
    print kthSmallest(arr, 0, n-1, k)  
    
    arr = [7, 10, 4, 3, 20, 15]
    n = len(arr)
    k = 4
    print kthSmallest(arr, 0, n-1, k)  
    

'''
Method 5
The idea is to randomly pick a pivot element. To implement randomized partition,
we use a random function, rand() to generate index between l and r, swap the element at 
randomly generated index with the last element, and finally call the standard partition
process which uses last element as pivot.
The worst case time complexity of the above solution is still O(n2). In worst case, the randomized
function may always pick a corner element. The expected time complexity of above randomized QuickSelect is Θ(n)
'''
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
