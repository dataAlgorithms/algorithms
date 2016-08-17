1. binary search
def binarySearch(theSeq, theValue):

    theSeq = sorted(theSeq)

    n = len(theSeq)

    low = 0
    high = n -1
    while low <= high:
        mid = (low + high) // 2
        if theValue == theSeq[mid]:
            return True
        elif theValue > theSeq[mid]:
            low = mid+1
        else:
            high = mid-1

    return False

'''
True
True
True
False
'''
if __name__ == "__main__":
    theSeq = [1, 7, 3, 21, 0, 27, 25]

    for theValue in [7, 0, 25, 22]:
        print binarySearch(theSeq, theValue)
        
2. Search at distinct array
# Returns index of key in distinct arr[l..h] if key is present
# otherwise returns -1
# If arr is not distinct, return True or False
def search(arr, key):

    n = len(arr)
    if len(set(arr)) == len(arr):
        result = recSearch(arr, 0, n-1, key)
    else:
        result = binarySearch(arr, key)

    return result

# binary search
def binarySearch(theSeq, theValue):

    theSeq = sorted(theSeq)
    n = len(theSeq)

    low = 0
    high = n -1
    while low <= high:
        mid = (low + high) // 2
        if theValue == theSeq[mid]:
            return True
        elif theValue > theSeq[mid]:
            low = mid+1
        else:
            high = mid-1

    return False

# Recursive search
def recSearch(arr, l, h, key):
    if l > h:
        return -1

    mid = (l+h) // 2
    if arr[mid] == key:
        return mid

    # If arr[l...mid] is sorted
    if arr[l] <= arr[mid]:
        # As this subarray is stored, we can quickly
        # check if key lies in half or other half
        if key >= arr[l] and key <= arr[mid]:
            return recSearch(arr, l, mid-1, key)

        return recSearch(arr, mid+1, h, key)

    # If arr[l...mid] is not sorted, then arr[mid...r]
    # must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return recSearch(arr, mid+1, h, key)

    return recSearch(arr, l, mid-1, key)

'''
6
-1
True
False
'''
if __name__ == "__main__":
    arr = [4, 5, 6, 7, 8,  9, 2, 1, 3]
    print search(arr, 2)
    print search(arr, 11)
    arr = [4, 5, 6, 7, 8, 8, 9, 2, 1,2, 3]
    print search(arr, 6)
    print search(arr, 11)
 
