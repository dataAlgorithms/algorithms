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
4, binarySearch that avoid overflow for (low+high)//2
'''
def binarySearchOverflow(theSeq, target):

    # get the length of theSeq
    n = len(theSeq)

    # loop
    low = 0
    high = n - 1
    while low <= high:
        #mid = (low+high) // 2
        if low % 2 == 1 and high % 2 == 1:
            mid = low // 2 + high // 2 + 1
        else:
            mid = low // 2 + high // 2
        if target == theSeq[mid]:
            return mid
        elif target < theSeq[mid]:
            high = mid-1
        else:
            low = mid+1

    return -1
   
'''
5
''' 
if __name__ == "__main__":
    target = 5
    theSeq = range(10)
    print binarySearchOverflow(theSeq, target)

'''
5. Given an array of N distinct integers, find floor value of input ‘key’

https://github.com/dataAlgorithms/algorithms/blob/master/searchSort/findFloorForSortedArr.py
'''

'''
6. Given a sorted array with possible duplicate elements.
 Find number of occurrences of input key in log N time
 
https://github.com/dataAlgorithms/algorithms/blob/master/searchSort/countOccurencesSortedArr.py
'''
