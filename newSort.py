# get random numbers
def getRandomNum(num=60):

    import random

    lottery_numbers = range(-1000, 1000)
    
    winning_numbers = random.sample(lottery_numbers, num)
    
    print winning_numbers
    return winning_numbers

#1. bubble sort
def bubbleSort(theSeq):

    n = len(theSeq)
    for i in range(n-1):
        for j in range(n-i-1):
            if theSeq[j] > theSeq[j+1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j+1]
                theSeq[j+1] = tmp
                
#2. insert sort
def insertSort(theSeq):

    n = len(theSeq)
    for i in range(1,n):
        pos = i
        pivot = theSeq[pos]
        while pos > 0 and pivot < theSeq[pos-1]:
            theSeq[pos] = theSeq[pos-1]
            pos = pos - 1

        theSeq[pos] = pivot
        
#3. select sort
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

#4. merge sort
def mergeSort(theSeq):

    n = len(theSeq)
    tmpList = [0] * n
    recMergeSort(theSeq, 0, n-1, tmpList)

def recMergeSort(theSeq, first, last, tmpList):

    if first >= last:
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
  
#5. quick sort
def quickSort(theSeq):

    n = len(theSeq)
    recQuickSort(theSeq, 0, n-1)

def recQuickSort(theSeq, first, last):

    if first >= last:
        return
    else:
        pos = partitionSeq(theSeq, first, last) 
        recQuickSort(theSeq, first, pos-1)
        recQuickSort(theSeq, pos+1, last)

def partitionSeq(theSeq, first, last):

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

    if first != right:
        theSeq[first] = theSeq[right]
        theSeq[right] = pivot

    return right
      
#6. heap sort
# The main function to sort an array of given size
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

#7. new heap sort
def newheapsort(sqc):                                 
    def down_heap(sqc, k, n):                            
        parent = sqc[k]                                  

        while 2*k+1 < n:                                 
            child = 2*k+1                                
            if child+1 < n and sqc[child] < sqc[child+1]:
                child += 1                               
            if parent >= sqc[child]:                     
                break                                    
            sqc[k] = sqc[child]                          
            k = child                                    
        sqc[k] = parent                                  

    size = len(sqc)                                      

    for i in range(size/2-1, -1, -1):                    
        down_heap(sqc, i, size)                          

    for i in range(size-1, 0, -1):                       
        sqc[0], sqc[i] = sqc[i], sqc[0]                  
        down_heap(sqc, 0, i)   
        
if __name__ == "__main__":
    print "Primary numbers:\r"
    theSeq = getRandomNum()
    
    print "Insert sorted numbers:\r"
    insertSort(theSeq)
    print theSeq
    
    print "\rPrimary numbers:\r"
    theSeq = getRandomNum()
    
    print "Bubble sorted numbers:\r"
    bubbleSort(theSeq)
    print theSeq
    
    print "\rPrimary numbers:\r"
    theSeq = getRandomNum()
    
    print "Select sorted numbers:\r"
    selectSort(theSeq)
    print theSeq
    
    print "\rPrimary numbers:\r"
    theSeq = getRandomNum()
    
    print "Merge sorted numbers:\r"
    mergeSort(theSeq)
    print theSeq
    
    print "\rPrimary numbers:\r"
    theSeq = getRandomNum()
    
    print "Quick sorted numbers:\r"
    quickSort(theSeq)
    print theSeq

    print "Heap sorted numbers:\r"
    heapSortMain(theSeq)
    print theSeq
