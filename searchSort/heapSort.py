'''
1. heap sort

Heap sort is a comparison based sorting technique based on Binary Heap data structure. 
It is similar to selection sort where we first find the maximum element and place 
the maximum element at the end. We repeat the same process for remaining element.

What is Binary Heap?
Let us first define a Complete Binary Tree. A complete binary tree is a binary tree in which every level, 
except possibly the last, is completely filled, and all nodes are as far left as possible (Source Wikipedia)
A Binary Heap is a Complete Binary Tree where items are stored in a special order 
such that value in a parent node is greater(or smaller) than the values in its two children nodes. 
The former is called as max heap and the latter is called min heap. The heap can be represented by binary tree or array.
Why array based representation for Binary Heap?
Since a Binary Heap is a Complete Binary Tree, it can be easily represented as array and array based 
representation is space efficient. If the parent node is stored at index I, the left child can be 
calculated by 2 * I + 1 and right child by 2 * I + 2 (assuming the indexing starts at 0).

Heap Sort Algorithm for sorting in increasing order:
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. 
Replace it with the last item of the heap followed by reducing the size of heap by 1. 
Finally, heapify the root of tree.
3. Repeat above steps until size of heap is greater than 1.

How to build the heap?
Heapify procedure can be applied to a node only if its children nodes are heapified. 
So the heapification must be performed in the bottom up order.
Lets understand with the help of an example:
Input data: 4, 10, 3, 5, 1
                 4(0)
                /   \
             10(1)   3(2)
            /   \
         5(3)    1(4)

The numbers in bracket represent the indices in the array
representation of data.

Applying heapify procedure to index 1:
                4(0)
                /   \
            10(1)    3(2)
           /   \
        5(3)    1(4)

Applying heapify procedure to index 0:
                10(0)
                /  \
             5(1)  3(2)
            /   \
         4(3)    1(4)
The heapify procedure calls itself recursively to build heap
 in top down manner.

Heap sort is an in-place algorithm.
Time Complexity: Time complexity of heapify is O(Logn). 
Time complexity of createAndBuildHeap() is O(n) 
and overall time complexity of Heap Sort is O(nLogn).
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

'''
3. Find k smallest element in the array
'''
# left child
def leftChild(i):

    return 2*i + 1

# right child
def rightChild(i):
   
    return 2*i + 2

# swap elements
def swapElements(a, i, j):

    a[i], a[j] = a[j], a[i]

# heapify min
def heapify(a, i, len_):

    largest = i

    left = leftChild(i)
    right = rightChild(i)

    if left <= len_ and a[largest] < a[left]:
        largest = left

    if right <= len_ and a[largest] < a[right]:
        largest = right

    if largest != i:
        swapElements(a, i, largest)
        heapify(a, largest, len_)
        
# create a min heap
def buildHeap(a, len_):

    i = len_/2 + 1
    while i >= 0:
        heapify(a, i, len_)
        i -= 1

# insert item into heap
def insertInHeap(a, K, element):
    a[0] = element
    heapify(a, 0, K)

# find k small elements
def kSmallElement(a, K):

    N = len(a)
    minHeap = [0] * K

    # Copy first K elements in another array
    for i in range(0, K):
        minHeap[i] = a[i]

    # Build max heap with those entered elements
    buildHeap(minHeap, K-1)

    for i in range(K, N):
        # If this number if less than root of max heap, insert it
        if a[i] <= minHeap[0]:
            insertInHeap(minHeap, K-1, a[i])

    return minHeap[0]

'''
[56, 32, 20, 36, 4, 7, 26, 22, 38, 13, 9, 25, 53, 21, 49, 27, 47, 29, 35, 45]
13
'''
if __name__ == "__main__":
    import random
    lottery_numbers = range(60)
    winning_numbers = random.sample(lottery_numbers, 20)
    a = winning_numbers 
    K = 4
    print a
    print kSmallElement(a, K)
    
'''
4. Find k largest element in a array
'''
#! coding=utf-8
'''
In min heap method we will create a min heap of size k which will store the k largest element. 
Initially we will create this min heap using the first k element of the given array say ��arr��. 

After creating min heap with first k element we will traverse rest of the given array i.e. 
from arr k+1 to n. As we have a min heap, smallest element of all the K largest element will be at the root. 
Now we will compare each element starting from the arr k+1 with the root of the min heap and if it is greater 
than root then we will replace the root with that element and call heapify on the root. This way we will get largest k element in the min heap.
'''
def heapify(res, k, i):

    smallest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < k and res[l] < res[smallest]:
        smallest = l

    if r < k and res[r] < res[smallest]:
        smallest = r

    if smallest != i:
        res[smallest], res[i] = res[i], res[smallest]

        heapify(res, k, smallest)

def findklargest(arr, res, n, k):

    # Copy the first k element into res array
    for i in range(0, k):
        res[i] = arr[i]

    # Build heap of the res array
    # by calling heapify on every parent node
    for i in range(k/2-1, -1, -1):
        heapify(res, k, i)

    # Check whether any element present in arr is
    # greater than the smallest element(root) of all the element
    # present in min heap
    for i in range(k, n):
        # If any element is greater then replace the root 
        # with this element
        if arr[i] > res[0]:
            res[0] = arr[i]
            heapify(res, k, 0)

    # now sort the min heap to get result 
    for i in range(k-1, -1, -1):
        res[0], res[i] = res[i], res[0]

'''
[36, 55, 52, 91, 59, 73, 54, 65, 52, 33]
[91, 73]
'''
if __name__ == "__main__":
    import random 
    arr = [random.randrange(100) for _ in range(10)]
    n = len(arr)
    k = 2
    res = [0] * k

    findklargest(arr, res, n, k)
    print arr
    print res
