def newrange(stop):
   i = 0
   while i < stop:
       yield i
       i += 1
       
#1. binary search with few comparation
def binarySearchFewComparation(theSeq, key):

    n = len(theSeq)
    l = 0
    r = n - 1
    while r - l > 1:
        m = (l+r) // 2
        if theSeq[m] <= key:
            l = m
        else:
            r = m

    if theSeq[l] == key:
        return l
    else:
        return -1

#2. binary search using iterative way
def binarySearchIter(theSeq, target):

    # get the length of theSeq
    n = len(theSeq)

    # loop
    low = 0
    high = n - 1
    while low <= high:
        mid = (low+high) // 2
        if target == theSeq[mid]:
            return mid
        elif target < theSeq[mid]:
            high = mid-1
        else:
            low = mid+1

    return -1

#3. binary search using recursive way
def binarySearchRec(theSeq, left, right, target):


    if left <= right:
        mid = (left + right) // 2
        if target == theSeq[mid]:
            return mid
        elif target < theSeq[mid]:
            return binarySearchRec(theSeq, left, mid-1, target)
        else:
            return binarySearchRec(theSeq, mid+1, right, target)

    return -1

'''
50
end-start: 0.000340122672242
50
end-start: 0.00017676115408
50
end-start: 0.000118315933832
'''
if __name__ == "__main__":
    theSeq = [i for i in newrange(10000000)]
    target = 50
    import time
    start = time.clock()
    print binarySearchIter(theSeq, target)
    end = time.clock()
    print 'end-start:', end-start

    start = time.clock()  
    print binarySearchRec(theSeq, 0, len(theSeq)-1, target)  
    end = time.clock()
    print 'end-start:', end-start

    start = time.clock()  
    print binarySearchFewComparation(theSeq, target)
    end = time.clock()
    print 'end-start:', end-start

'''
4. Given an array of N distinct sorted integers, find floor value of input ‘key’. Say, A = {-1, 2, 3, 5, 6, 8, 9, 10} and key = 7, we should return 6 as outcome.
'''
def floor(aList, key):
    
    def toFloor(aList, l, r, key):
    
        while r-l > 1:
            m = (l+r) // 2
            if aList[m] <= key:
                l = m
            else:
                r = m
    
        return aList[l]

    # add error check if key < aList[0]
    if key < aList[0]:
        return -1

    return toFloor(aList, 0, len(aList)-1, key)

'''
6
'''
if __name__ == "__main__":
    aList = [-1, 2, 3, 5, 6, 8, 9, 10]
    key = 7
    print floor(aList, key)

'''
5. Problem Statement: Given a sorted array with possible duplicate elements.
 Find number of occurrences of input ‘key’ in log N time
'''
def getRightPosition(aList, l, r, key):

    while r -l > 1:
        m = (l+r) // 2
        if aList[m] <= key:
            l = m
        else:
            r = m

    return l

def getLeftPosition(aList, l, r, key):

    while r - l > 1:
        m = (l+r) // 2
        if aList[m] >= key:
            r = m
        else:
            l = m

    return r

def countOccurences(aList, key):
    left = getLeftPosition(aList, -1, len(aList)-1 , key)
    right = getRightPosition(aList, 0, len(aList), key)

    if aList[left] == key and key == aList[right]:
        return right - left + 1
    else:
        return 0

'''
2
0
1
'''
if __name__ == "__main__":
    aList = [-1, 2, 3, 5, 6, 6, 8, 9, 10]
    print countOccurences(aList, 6)
    print countOccurences(aList, 11)
    print countOccurences(aList, 2)

'''
6. find minimum element in a sorted and rotated-array/
'''
def findMin(arr, low, high):

    # The condition is needed to handle the case
    # when array is not rotated at all
    if high < low:
        return arr[0]

    # If there is only one element left
    if high == low:
        return arr[low]

    # Find mid
    mid = (low + high) // 2

    # check if element (mid+1) is minimum element,
    # consider the cases like {3, 4, 5, 1, 2}
    if mid < high and arr[mid+1] < arr[mid]:
        return arr[mid+1]

    # check if mid itself is minimum element
    if mid > low and arr[mid] < arr[mid-1]:
        return arr[mid]

    # decide whether we need to go to left half or right half
    if arr[high] > arr[mid]:
        return findMin(arr, low, mid-1)

    return findMin(arr, mid+1, high)

'''
1
'''
if __name__ == "__main__":
   arr = [5, 6, 1, 2, 3, 4]
   print findMin(arr, 0, len(arr)-1)
