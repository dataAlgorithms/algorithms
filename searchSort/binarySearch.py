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
   first decrease, then increase
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

'''
7. Find a peak element using divide and conquer
'''
def findPeak(arr):

    n = len(arr)
    
    low = 0
    high = n -  1
    while low <= high:
        mid = (low + high) // 2
        
        if (mid == 0 or arr[mid-1] <= arr[mid]) and \
             (mid == n-1 or arr[mid+1] <= arr[mid]):
            return arr[mid]
        elif mid > 0 and arr[mid-1] > arr[mid]:
            high = mid -1
        else:
            low = mid + 1

    return -1

'''
20
'''
if __name__ == "__main__":
    arr = [10,20,15,2,23,90,67]
    print findPeak(arr)
    
'''
8. Find all peak elements
'''
def findAllPeak(A):

    left = 0
    right = len(A) - 1
    tmpList = []
    while left + 1 < right:
        mid = left + (right - left)/2
        if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
            tmpList.append(mid)
            left = right
            right = len(A) -1
            continue
        if A[mid] == left:
            right = mid
        elif A[mid] == right:
            left = mid
        elif A[mid] < A[left]:
            right = mid
        elif A[mid] < A[right]:
            left = mid
        elif A[mid] > A[mid+1]:
            right = mid
        else:
            left = mid
     
    if A[left] > A[left-1] and A[left] > A[left+1]:
        tmpList.append(left)
    if A[right] > A[right-1] and A[right] > A[right+1]:
        tmpList.append(right)
        
    if len(tmpList) != 0:
        return tmpList
    else:
        return -1
    
'''
20 90
'''
if __name__ == "__main__":
    arr = [10,20,15,2,23,90,67]
    for i in findAllPeak(arr):
        print arr[i],

'''
9. Fixed point
'''
'''
Find a Fixed Point in a given array
Given an array of n distinct integers sorted in ascending order,
write a function that returns a Fixed Point in the array,
if there is any Fixed Point present in array, else returns -1.
Fixed Point in an array is an index i such that arr[i] is equal to i.
Note that integers in array can be negative.
'''

# use liner search
def fixedPointLinerSearchAll(arr):

    tmpList = []

    n = len(arr)
    for i in range(n):
        if arr[i] == i:
            tmpList.append(i)

    if len(tmpList) != 0:
        return tmpList
    else:
        return -1

# use binary search
def fixedPointBinarySearchOne(arr):

    n = len(arr)
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high) // 2
        if mid == arr[mid]:
            return mid
        elif mid > arr[mid]:
            low = mid+1
        else:
            high = mid-1

    return -1

'''
[3,5,6]
3
'''
if __name__ == "__main__":
    arr = [-10, -1, 0, 3, 10, 5, 6, 50, 100]
    print fixedPointLinerSearchAll(arr)
    print fixedPointBinarySearchOne(arr)

'''
10. Count the number of occurrences in a sorted array
'''

# liner search
def occurenceSortedSeqLS(sortedList, key):

    count = 0
    flag = 0
    for item in sortedList:
        if item == key:
            flag = 1
            count += 1

    if flag == 0:
        return -1
    else:
        return count

# binary search 
'''
 Use Binary search to get index of the first occurrence of x in arr[]. Let the index of the first occurrence be i.
 Use Binary search to get index of the last occurrence of x in arr[]. Let the index of the last occurrence be j.
 Return (j – i + 1)
'''
def occurenceSortedSeqBS(sortedList, key):

    def first(arr, low, high, key, n):
        if high >= low:
            mid = (low+high) // 2
            if (mid == 0 or key > arr[mid-1]) and arr[mid] == key:
                return mid
            elif key > arr[mid]:
                return first(arr, (mid+1), high, key, n)
            else:
                return first(arr, low, (mid-1), key, n)

        return -1

    def last(arr, low, high, key, n):
        if high >= low:
            mid = (low+high) // 2
            if (mid == n-1 or key < arr[mid+1]) and arr[mid] == key:
                return mid
            elif key < arr[mid]:
                return last(arr, low, (mid-1), key, n)
            else:
                return last(arr, (mid+1), high, key, n)

        return -1

    # get the length
    n = len(sortedList)

    # get the index of first occurence of key
    i = first(sortedList, 0, n-1, key, n)

    if i == -1:
        return i

    # get the index of last occurence of key
    j = last(sortedList, i, n-1, key, n)

    # return count
    return j-i+1

'''
2
2
4
4
1
1
-1
-1
'''
if __name__ == "__main__":
    sortedList = [1, 1, 2, 2, 2, 2, 3]
    for key in [1, 2, 3, 4]:
        print occurenceSortedSeqLS(sortedList, key)
        print occurenceSortedSeqBS(sortedList, key)
   
'''
11. Median of two sorted arrays
'''

# Simply count while merging
'''
Use merge procedure of merge sort. Keep track of count while comparing elements of two arrays. If count becomes n(For 2n elements), we have reached the median. Take the average of the elements at indexes n-1 and n in the merged array
'''
def simpleGetMedian(ar1, ar2):

    n = len(ar1)
    i = 0
    j = 0
    m1 = -1
    m2 = -1

    '''
    Since there are 2n elements, median will be average
    of elements at index n-1 and n in the array obtained after
     merging ar1 and ar2
    '''
    for count in range(n+1):
        '''
        Below is to handle case where all elements of ar1[] are
        smaller than smallest(or first) element of ar2[]
        '''
        if i == n:
            m1 = m2
            m2 = ar2[0]
            break

        elif j == n:
            '''
            Below is to handle case where all elements of ar2[] are
            smaller than smallest(or first) element of ar1[]
            '''
            m1 = m2
            m2 = ar1[0]
            break

        if ar1[i] < ar2[j]:
            m1 = m2
            m2 = ar1[i]
            i += 1
        else:
            m1 = m2
            m2 = ar2[j]
            j += 1

    return (m1 + m2) * 0.5


'''
find median sorted array using binary search
'''
def getMedianDC(A, B):

    def findKth(A, B, k, aStart, aEnd, bStart, bEnd):
        aLen = aEnd - aStart + 1
        bLen = bEnd - bStart + 1

        # Handle special cases
        if aLen == 0:
            return B[bStart + k]
        if bLen == 0:
            return A[aStart + k]
        if k == 0:
            if A[aStart] < B[bStart]:
                return A[aStart]
            else:
                return B[bStart]

        aMid = aLen * k / (aLen + bLen)
        bMid = k - aMid - 1

        aMid = aMid + aStart
        bMid = bMid + bStart

        if A[aMid] > B[bMid]:
            k = k - (bMid - bStart + 1)
            aEnd = aMid
            bStart = bMid + 1
        else:
            k = k - (aMid - aStart + 1)
            bEnd = bMid
            aStart = aMid + 1

        return findKth(A, B, k, aStart, aEnd, bStart, bEnd)
    m = len(A)
    n = len(B)

    if (m+n)%2 != 0:
        return findKth(A, B, (m+n)/2, 0, m-1, 0, n-1)
    else:
        return (findKth(A, B, (m+n)/2, 0, m-1, 0, n-1) + \
                findKth(A, B, (m+n)/2-1, 0, m-1, 0, n-1)) * 0.5

'''
16.0
16.0
2.5
2.5
'''
if __name__ == "__main__":
    ar1 = [1, 12, 15, 26, 38]
    ar2 = [2, 13, 17, 30, 45]
    print simpleGetMedian(ar1, ar2)
    print getMedianDC(ar1, ar2)
    ar1 = [1, 2]
    ar2 = [3, 4]
    print simpleGetMedian(ar1, ar2)
    print getMedianDC(ar1, ar2)

'''
12. Find the maximum element in an array which is first increasing and then decreasing
Given an array of integers which is initially increasing and then decreasing, 
find the maximum value in the array


Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
Output: 500

Input: arr[] = {1, 3, 50, 10, 9, 7, 6}
Output: 50

Corner case (No decreasing part)
Input: arr[] = {10, 20, 30, 40, 50}
Output: 50

Corner case (No increasing part)
Input: arr[] = {120, 100, 80, 20, 0}
Output: 120
'''

# Use liear search
def findMaximumLS(arr):

    low = 0
    high = len(arr) - 1
    theMax = arr[low]
    for i in range(low, high+1):
        if arr[i] > theMax:
            theMax = arr[i]

    return theMax

# Use binary search
def findMaximumBS(arr):

    def findMaximum(arr, low, high):
        # Only one element is present in arr[low..high]
        if low == high:
            return arr[low]

        # If there are two elements and first is greater then
        # the first element if maximum
        if (high == low + 1) and arr[low] >= arr[high]:
            return arr[low]

        # If there are two elements and second is greater then
        # the second element is maximum
        if (high == low + 1) and arr[low] < arr[high]:
            return arr[high]

        mid = (low + high) // 2

        # If we reach a point where arr[mid] is greater than both of
        # its adjacent elements arr[mid-1] and arr[mid+1], then arr[mid]
        # is the maximum element
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
            return arr[mid]

        # If arr[mid] is greater than the next element and smaller than the previous
        # element then maximum lies on left side of mid 
        if arr[mid] > arr[mid+1] and arr[mid] < arr[mid-1]:
            return findMaximum(arr, low, mid-1)
        else: # when arr[mid] is greater than arr[mid-1] and smaller than arr[mid+1]
            return findMaximum(arr, mid+1, high)

    return findMaximum(arr, 0, len(arr)-1)
            
if __name__ == "__main__":
    arr = [1, 30, 40, 50, 60, 70, 23, 20]
    print findMaximumLS(arr)
    print findMaximumBS(arr)

'''
13, binarySearch that avoid overflow for (low+high)//2
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
