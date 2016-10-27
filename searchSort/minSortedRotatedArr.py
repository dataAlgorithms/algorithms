'''
 find minimum element in a sorted and rotated-array/
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
