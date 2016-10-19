#! coding=utf-8

'''
1. quickSort (use last item as pivot)
'''

def quickSort(theSeq):

    def recQuickSort(theSeq, first, last):
    
        if first >= last:
            return
        else:
            pos = partitionSeq(theSeq, first, last)
            recQuickSort(theSeq, first, pos-1)
            recQuickSort(theSeq, pos+1, last)
    
    
    def partitionSeq(theSeq, first, last):
    
        x = theSeq[last]
        i = first - 1
    
        for j in range(first, last):
            if theSeq[j] <= x:
                i += 1
                theSeq[i],theSeq[j] = theSeq[j],theSeq[i]
    
        theSeq[i+1],theSeq[last] = theSeq[last],theSeq[i+1]
    
        return i+1
    
    n = len(theSeq)
    recQuickSort(theSeq, 0, n-1)
    
    
'''
2. quickSort ( use the first item as pivot)
'''
def quickSortNew(theSeq):

    def recQuickSort(theSeq, first, last):
    
        if first >= last:
            return
        else:
            pos = partitionSeqNew(theSeq, first, last)
            recQuickSort(theSeq, first, pos-1)
            recQuickSort(theSeq, pos+1, last)
    
    def partitionSeqNew(theSeq, first, last):
        
        pivot = theSeq[first]
        left = first + 1
        right = last 
        
        while left <= right:
            while left <= right and theSeq[left] <= pivot:
                left += 1
                
            while right >= left and theSeq[right] >= pivot:
                right -= 1
                
            if left < right:
                theSeq[left], theSeq[right] = theSeq[right], theSeq[left]
                
        theSeq[first] = theSeq[right]
        theSeq[right] = pivot
        
        return right
    
    n = len(theSeq)
    recQuickSort(theSeq, 0, n-1)
  
'''
3. quick sort (Reducing worst case space to Log n)
'''
  
def quickSortOpt(aList, low, high):

    def partitionSeq(theSeq, first, last):
    
        x = theSeq[last]
        i = first - 1
    
        for j in range(first, last):
            if theSeq[j] <= x:
                i += 1
                theSeq[i],theSeq[j] = theSeq[j],theSeq[i]
    
        theSeq[i+1],theSeq[last] = theSeq[last],theSeq[i+1]
    
        return i+1

    while low < high:
        #pi is partitioning index, arr[p] is now at right place
        pi = partitionSeq(aList, low, high)

        # If left part is smaller, then recur for left
        # part and handle right part iteratively
        if pi - low < high - pi:
            quickSortOpt(aList, low, pi-1)
            low = pi + 1
        else:
            # Else recur for right part
            quickSortOpt(aList, pi+1, high)
            high = pi - 1
            
'''
aList (sorted before): [69, 71, 86, 41, 66, 1, 66, 64, 37, 75, 5, 92, 48, 49, 88, 45, 56, 46, 1, 99]
aList (sorted after): [1, 1, 5, 37, 41, 45, 46, 48, 49, 56, 64, 66, 66, 69, 71, 75, 86, 88, 92, 99]

bList (new sorted before): [69, 71, 86, 41, 66, 1, 66, 64, 37, 75, 5, 92, 48, 49, 88, 45, 56, 46, 1, 99]
bList (new sorted after): [1, 1, 5, 37, 41, 45, 46, 48, 49, 56, 64, 66, 66, 69, 71, 75, 86, 88, 92, 99]

cList (optimize sorted before): [69, 71, 86, 41, 66, 1, 66, 64, 37, 75, 5, 92, 48, 49, 88, 45, 56, 46, 1, 99]
cList (optimize sorted after): [1, 1, 5, 37, 41, 45, 46, 48, 49, 56, 64, 66, 66, 69, 71, 75, 86, 88, 92, 99]
'''
if __name__ == "__main__":
    
    import random
    aList = [random.randrange(100) % 100 for _ in range(20)]
    bList = [item for item in aList]
    cList = [item for item in aList]
    
    print 'aList (sorted before):', aList
    quickSort(aList)
    print 'aList (sorted after):', aList       
    
    print ''
    print 'bList (new sorted before):', bList
    quickSort(bList)
    print 'bList (new sorted after):', bList         
    
    print ''
    print 'cList (optimize sorted before):', cList
    quickSort(cList)
    print 'cList (optimize sorted after):', cList       

    '''
4. Iterative quick sort
The above implementation can be optimized in many ways
1) The above implementation uses last index as pivot. This causes worst-case behavior on already sorted arrays, 
which is a commonly occurring case. The problem can be solved by choosing either a random index for the pivot, 
or choosing the middle index of the partition or choosing the median of the first, 
middle and last element of the partition for the pivot. (See this for details)

2) To reduce the recursion depth, recur first for the smaller half of the array, 
and use a tail call to recurse into the other.

3) Insertion sort works better for small subarrays. Insertion sort can be used for invocations on such small arrays 
(i.e. where the length is less than a threshold t determined experimentally). For example, 
this library implementation of qsort uses insertion sort below size 7.

Despite above optimizations, the function remains recursive and uses function call stack to 
store intermediate values of l and h. The function call stack stores other bookkeeping information 
together with parameters. Also, function calls involve overheads like storing activation record 
of the caller function and then resuming execution.

The above function can be easily converted to iterative version with the help of an auxiliary stack. 
'''
# The function is the same in both iterative and recursive
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1],arr[h] = arr[h], arr[i+1]
    return i+1

# Function to do quick sort
# arr[] ..array to be sorted
# l .. starting index
# h .. ending index
def quickSortIterative(arr, l, h):

    # Create an auxiliary stack
    size = h -l + 1
    stack = [0] * size

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in 
        # sorted array
        p = partition(arr, l, h)

        # If there are elements on left side of pivot
        # then push left side to stack
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot
        # then push right side to stack
        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

'''
Sorted array is: [1, 2, 2, 3, 3, 3, 4, 5]
Sorted array is: [-1, 2, 3, 4]
'''
if __name__ == "__main__":
    for arr in [[4, 3, 5, 2, 1, 3, 2, 3], [2, -1, 3, 4]]:
        n = len(arr)
        quickSortIterative(arr, 0, n-1)
        print "Sorted array is:", arr

'''
5. QuickSort for Single LinkedList
In partition(), we consider last element as pivot. We traverse through the current list and 
if a node has value greater than pivot, we move it after tail. If the node has smaller value, 
we keep it at its current position.

In QuickSortRecur(), we first call partition() which places pivot at correct position 
and returns pivot. After pivot is placed at correct position, we find tail node of 
left side (list before pivot) and recur for left list. Finally, we recur for right list.
'''
# Implement Bag using linked list
class LinkedList:
    # Init
    def __init__(self):
        self._head = None
        self._size = 0

    # Length
    def __len__(self):
        return self._size

    # Contain
    def __contains__(self, target):
        curNode = self._head
        while curNode is not None and curNode.data != target:
            curNode = curNode.next

        return curNode is not None

    # Add
    def add(self, element):
        newItem = LinkedListNode(element)
        newItem.next = self._head
        self._head = newItem
        self._size += 1

    # Remove
    def remove(self, element):
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.data != element:
            preNode = curNode
            curNode = curNode.next

        assert curNode is not None, "element is not in the Bag."
        self._size -= 1

        if curNode is self._head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next

        return curNode.data

    # Iter
    def __iter__(self):
        return LinkedListBagIterator(self._head)

# Bag storage
class LinkedListNode:
    # Init
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Bag iter
class LinkedListBagIterator:
    # Init
    def __init__(self, head):
        self.curNode = head
    def __iter__(self):
        return self
    def next(self):
        if self.curNode is not None:
            value = self.curNode.data
            self.curNode = self.curNode.next
            return value
        else:
            raise StopIteration

# Returns the last node of the list
def getTail(curNode):

    while curNode is not None and curNode.next is not None:
        curNode = curNode.next

    return curNode

# Partitions the list taking the last element as the pivot
def partition(head, end, newHead, newEnd):

    pivot = end
    prev = None
    cur = head
    tail = pivot

    # During partition, both the head and end of the list might change
    # which is updated in the newHead and newEnd variables
    while cur != pivot:
        if cur.data < pivot.data:
            # First node htat has a value less than the pivot
            # becomes the new head
            if newHead is None:
                newHead = cur

            prev = cur
            cur = cur.next
        else: 
            # If cur node is greater than pivot
            # Move cur node to next of tail, and change tail
            if prev is not None:
                prev.next = cur.next
            tmp = cur.next
            cur.next = None
            tail.next = cur
            tail = cur
            cur = tmp

    # If the pivot data is the smallest element in the current list
    # pivot becomes the head
    if newHead is None:
        newHead = pivot

    # Update newEnd to the current last node
    newEnd = tail

    # Return the pivot, newHead, newEnd
    return pivot, newHead, newEnd

# Here the sorting happends exclusive of the end node
def quickSortRecur(head, end):

    # Base condition
    if head is None or head == end:
        return head

    newHead = None
    newEnd = None

    # Partition the list, newHead and newEnd will be updated
    # by the partition function
    pivot, newHead, newEnd = partition(head, end, newHead, newEnd)

    # If pivot is the smallest element 
    # no need to recur for the left part
    if newHead != pivot:
        # Set the node before the pivot node as None
        tmp = newHead
        while tmp.next != pivot:
            tmp = tmp.next
        tmp.next = None

        # Recur for the list before pivot
        newHead = quickSortRecur(newHead, tmp)

        # Change next of last node of the left half to pivot
        tmp = getTail(newHead)
        tmp.next = pivot

    # Recur for the list after the  pivot element
    pivot.next = quickSortRecur(pivot.next, newEnd)

    return newHead

# Main function for quick sort 
# Wrapper over recursive function quickSortRecur
def quickSort(headRef):

    newHead = quickSortRecur(headRef, getTail(headRef))
    return newHead

'''
...Sort before
ECON-111 HIST-350 ECON-101 HIST-340 MATH-121 CSCI-112 

...Sort after
CSCI-112 ECON-101 ECON-111 HIST-340 HIST-350 MATH-121
'''
if __name__ == "__main__":
    smith = LinkedList()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    smith.add('HIST-350')
    smith.add('ECON-111')
    
    print '...Sort before'
    for item in smith:
        print item,
        
    newsmith = quickSort(smith._head)
    print '\r\r...Sort after'
    while newsmith is not None:
        print newsmith.data,
        newsmith = newsmith.next
