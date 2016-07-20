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

    def partitionSeq(theSeq, p, r):

        x = theSeq[r]
        i = p - 1
        for j in range(p, r):
            if theSeq[j] <= x:
                i = i + 1
                theSeq[i],theSeq[j] = theSeq[j],theSeq[i]

        theSeq[i+1],theSeq[r] = theSeq[r],theSeq[i+1]
        return i+1

    def recQuickSort(theSeq, first, last):

        if first >= last:
            return
        else:
            pos = partitionSeq(theSeq, first, last)
            recQuickSort(theSeq, first, pos-1)
            recQuickSort(theSeq, pos+1, last)

    n = len(theSeq)
    recQuickSort(theSeq, 0, n-1)

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
  
#7. count sort
def countSort(theSeq):

    def countSortMain(A, k):
        n = len(A)

        B = []
        for i in range(n):
            B.append(0)

        C = []
        for i in range(k):
            C.append(0)

        for j in range(0, n):
            C[A[j]] = C[A[j]] + 1

        for i in range(1, k):
            C[i] = C[i] + C[i-1]

        for j in range(n-1, -1, -1): 
            B[C[A[j]]-1] = A[j]
            C[A[j]] = C[A[j]] - 1

        return B


    def diffMaxMin(A):

        small = A[0]
        large = A[0]
        for i in A:
            if i < small:
                small = i

            if i > large:
                large = i

        return large - small + 1


    k = diffMaxMin(theSeq)
    theSeq = countSortMain(theSeq, k)

    flag = 0
    for i in range(len(theSeq)):

        if theSeq[i] < 0:
            flag = 1
            break

    if flag == 1:
        newSeq = theSeq[:i]
        tmpSeq = theSeq[i:]

        tmpSeq.extend(newSeq)
    else:
        tmpSeq = theSeq 
        
    return tmpSeq
    
#8. radix sort
def radixSort(a, radix=10, debug=1):

    def getMaxDigitNum(a, radix=10, debug=1):
        intList = [int(item) for item in a]
        maxItem = max(intList)

        count = 0
        j = 1
        while maxItem  >= 1:
            maxItem  /= j
            count += 1
            j *= radix

        if debug == 1:
            print count

        return count

    k = getMaxDigitNum(a, radix=10, debug=1)
    buckets = [[] for i in range(radix)]
    for i in range(1, k+1):
        for key in a:
            buckets[key%(radix**i)/(radix**(i-1))].append(key)

        del a[:]
        for each in buckets:
            a.extend(each)

        buckets = [[] for i in range(radix)]

    if debug == 1:
        print a

    return a
    
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
    heapSort(theSeq)
    print theSeq
