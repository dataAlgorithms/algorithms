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
