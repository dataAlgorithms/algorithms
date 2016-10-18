'''
1. Merge sort
  use divide and conquer way to sort
'''
def mergeSort(theSeq):

    # get the length 
    n = len(theSeq)

    # tmpList to store the item
    tmpList = [0] * n

    # rec merge sort
    recMergeSort(theSeq, 0, n-1, tmpList)

def recMergeSort(theSeq, first, last, tmpList):

    if first == last:
        return
    else:
        mid = (first + last) // 2
        recMergeSort(theSeq, first, mid, tmpList)
        recMergeSort(theSeq, mid+1, last, tmpList)

        mergeVitualSeq(theSeq, first, mid+1, last+1, tmpList)

def mergeVitualSeq(theSeq, left, right, end, tmpList):

    a = left
    b = right
    m = 0
    while a < right and b < end:
        if theSeq[a] < theSeq[b]:
            tmpList[m] = theSeq[a]
            m += 1
            a += 1
        else:
            tmpList[m] = theSeq[b]
            m += 1
            b += 1

    while a < right:
        tmpList[m] = theSeq[a]
        m += 1
        a += 1

    while b < end:
        tmpList[m] = theSeq[b]
        m += 1
        b += 1

    for i in range(end-left):
        theSeq[left+i] = tmpList[i]

def test_mergeSort():
    
    # do the linear search
    theValues = [35, -85, -92, -52, -496, 216, -860, 435, -976, -966, -919, 950, 605, -547, 537, -311, -20, 53, 856, 50, -210, 580, -979, 912, 275, -701, -800, -953, -2, -769, 572, 509, 723, -490, -957, -341, -899, 263, -109, -895, 989, 345, -282, 547, -678, -304, -998, 610, 478, -333, -783, -915, -454, -665, 729, -303, 78, 652, 228, 394]
    mergeSort(theValues)
    
    print theValues
        
'''
[-998, -979, -976, -966, -957, -953, -919, -915, -899, -895, -860, -800, -783, -769, -701, -678, -665, -547, -496, -490, -454, -341, -333, -311, -304, -303, -282, -210, -109, -92, -85, -52, -20, -2, 35, 50, 53, 78, 216, 228, 263, 275, 345, 394, 435, 478, 509, 537, 547, 572, 580, 605, 610, 652, 723, 729, 856, 912, 950, 989]
'''
if __name__ == "__main__":
    test_mergeSort()

'''
2. LinkedList sort using merge sort
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
        
# Sorts a linked list using merge sort.
# A new head reference is returned
def llistMergeSort(theList):

    # If the list is empty (base case), return None
    if theList is None:
        return None
    elif theList.next is None:
        return theList       

    # Split the linked list into two sublists of equal size
    rightList = _splitLinkedList(theList)
    leftList = theList

    #print 'rightList:', rightList
    #print 'leftlist:', leftList 
    
    # Perform the same operation on the left half
    leftList = llistMergeSort(leftList)

    # ... and the right half
    rightList = llistMergeSort(rightList)

    # Merge the two ordered sublists
    theList = _mergeLinkedLists(leftList, rightList)

    # Return the head pointer of the ordered sublist
    return theList

# Splits a linked list at the midpoint to create two sublists.
# The head reference of the right sublists is returned
# The left sublist is still referenced by the original head reference
def _splitLinkedList(subList):
    
    # Assign a reference to the first and second nodes in the list
    midPoint = subList
    curNode = midPoint.next

    # Iterate through the list until curNode falls off the end
    while curNode is not None:
        #print 'curNode:', curNode
        # Advance curNode to the next node
        curNode = curNode.next

        # If there are more nodes, advance curNode again the midPoint once
        if curNode is not None:
            midPoint = midPoint.next
            curNode = curNode.next


    # Set rightList as the head pointer to the right sublist
    rightList = midPoint.next
    # Unlink the right sub list from the left sublist
    midPoint.next = None

    # Return the right sub list head reference
    return rightList

def _splitLinkedListNew(source):

    if source is None or source.next is None:
        frontRef = source
        backRef = None
    else:
        slow = source
        fast = source.next

        # Advance fast two nodes, slow one node
        while fast is not None:
            fast = fast.next
            if fast is not None:
                slow = slow.next
                fast = fast.next

        # slow is before the midpoint in the list, so split it in 
        # two at that point
        frontRef = source
        backRef = slow.next
        slow.next = None

    return frontRef, backRef

# Merges two sorted linked ist:
# return head reference for the new list
def _mergeLinkedLists(subListA, subListB):
    if subListA is None:
        return subListB 
    elif subListB is None:
        return subListA
    
    # Create a dummy node and insert it at the front of the list
    newList = LinkedListNode(None) 

    newTail = newList

    # Append nodes to the new list until one list is empty
    while subListA is not None and subListB is not None:
        if subListA.data <= subListB.data:
            newTail.next = subListA
            subListA = subListA.next
        else:
            newTail.next = subListB
            subListB = subListB.next
        
        newTail = newTail.next
        newTail.next = None

    # If self list contains more terms, append them
    if subListA is not None:
        newTail.next = subListA
    else:
        newTail.next = subListB

    # Return the new merged list, which begins with the first node after
    # the dummy node
    return newList.next

def _mergeLinkedListsNew(subListA, subListB):
    result = LinkedListNode(None)
 
    if subListA is None:
        return subListB 
    elif subListB is None:
        return subListA

    if subListA.data <= subListB.data:
        result = subListA
        result.next = _mergeLinkedLists(subListA.next, subListB)
    else:
        result = subListB
        result.next = _mergeLinkedLists(subListA, subListB.next)

    return result

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
        
    smith = llistMergeSort(smith._head)
    print '\r\r...Sort after'
    while smith is not None:
        print smith.data,
        smith = smith.next
        
'''
3. Count Inversions in an array 
'''
def getInvCountNV(arr):
    '''
    Use native way to get inverse count
    '''
    
    n = len(arr)
    inv_count = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count

'''
This function sorts the input array and returns the 
number of inversions in the array
'''
def mergeSort(arr):

    n = len(arr)
    temp = [0] * n
    return _mergeSort(arr, temp, 0, n-1)

'''
An anxiliary recursive function that sorts the input array and
returns the number of inversions in the array
'''
def _mergeSort(arr, temp, left, right):

    inv_count = 0
    if right > left:
        mid = (left + right) // 2

        inv_count = _mergeSort(arr, temp, left, mid)
        inv_count += _mergeSort(arr, temp, mid+1, right)

        inv_count += merge(arr, temp, left, mid+1, right)

    print 'right:', right
    print 'left:', left 

    return inv_count

'''
Merges two sorted arrays and returns inversion count in the array
'''
def merge(arr, temp, left, mid, right):
    inv_count = 0

    i = left
    j = mid
    k = left
    while (i <= mid -1) and (j <= right):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

            inv_count = inv_count + (mid -i)

    # Copy the remaining elements of left subarray
    while i <= mid -1:
        temp[k] = arr[i]
        k += 1
        i += 1

    # Copy the remaining elementsof right subarray
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    # Copy merged elements to original array
    for i in range(left, right+1):
        arr[i] = temp[i]

    return inv_count

'''
5
'''
if __name__ == "__main__":
    arr = [1, 20, 6, 4, 5]
    print mergeSort(arr)
