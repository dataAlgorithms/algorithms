# get random numbers
def getRandomNum(num=60):

    import random

    lottery_numbers = range(-1000, 1000)
    
    winning_numbers = random.sample(lottery_numbers, num)
    
    print winning_numbers
    return winning_numbers

# bubble sort
def bubbleSort(theSeq):

    n = len(theSeq)
    for i in range(n-1):
        for j in range(n-i-1):
            if theSeq[j] > theSeq[j+1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j+1]
                theSeq[j+1] = tmp
                
# insert sort
def insertSort(theSeq):

    n = len(theSeq)
    for i in range(1,n):
        pos = i
        pivot = theSeq[pos]
        while pos > 0 and pivot < theSeq[pos-1]:
            theSeq[pos] = theSeq[pos-1]
            pos = pos - 1

        theSeq[pos] = pivot
        
# select sort
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

# merge sort
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
