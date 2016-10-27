'''
1. Find a peak element using divide and conquer
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
2. Find all peak elements
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
3. Find the maximum element in an array which is first increasing and then decreasing
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
