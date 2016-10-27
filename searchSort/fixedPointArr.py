'''
1. Fixed point
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
