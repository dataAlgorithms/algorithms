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
 
3. Interpolation search 
# Interpolation search 

def interpolation_search(sorted_list, to_find):

    low = 0
    high = len(sorted_list) - 1

    while sorted_list[low] <= to_find and sorted_list[high] >= to_find:
        mid = (low + ((to_find - sorted_list[low]) * (high - low)) \
                / (sorted_list[high] - sorted_list[low]))

        if sorted_list[mid] < to_find:
            low = mid + 1
        elif sorted_list[mid] < to_find:
            high = mid - 1
        else:
            return mid

    if sorted_list[low] == to_find:
        return low

    return None

'''
Numbers:
-100 -6 0 1 5 14 15 26 99

Number 15 is at index 6
'''
if __name__ == "__main__":
    # Pre-sorted numbers
    numbers = [-100, -6, 0, 1, 5, 14, 15, 26, 99]
    value = 15
    
    # Print numbers to search
    print 'Numbers:'
    print ' '.join([str(i) for i in numbers])
    
    # Find the index of 'value'
    index = interpolation_search(numbers, value)

    # Print the index where 'value' is located
    print '\nNumber %d is at index %d' % (value, index)
