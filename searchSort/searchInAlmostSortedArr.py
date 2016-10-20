'''
Search in an almost sorted array
A recursive binary search based function.
It returns index of x in given array arr[l..r] is present
otherwise -1
'''
def binarySearch(arr, l, r, x):

    if r >= l:
        mid = l + (r -l)// 2

        # If the element is present at one of the middle 3 positions
        if arr[mid] == x:
            return mid

        if mid > 1 and arr[mid-1] == x:
            return mid - 1
        if mid < r and arr[mid+1] == x:
            return mid + 1

        # If element is smaller than mid, then it can only
        # be present in left subarray
        if arr[mid] > x:
            return binarySearch(arr, l, mid-2, x)
        # Else the element can only be present in right subarray
        return binarySearch(arr, mid+2, r, x)

    return -1

'''
3
2
-1
'''
if __name__ == "__main__":
    for arr, x in [[[3, 2, 10, 4, 40], 4], [[10, 3, 40, 20, 50, 80, 70], 40], [[10, 3, 40, 20, 50, 80, 70], 90]]:
        result = binarySearch(arr, 0, n-1, x)
        print result
