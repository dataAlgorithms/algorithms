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
