'''
Search in an almost sorted array
Given an array which is sorted, but after sorting some elements are moved to either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1].
 Write an efficient function to search an element in this array. Basically the element arr[i] can only be swapped with either arr[i+1] or arr[i-1].

For example consider the array {2, 3, 10, 4, 40}, 4 is moved to next position and 10 is moved to previous position.

Example:

Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
Output: 2 
Output is index of 40 in given array

Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 90
Output: -1
-1 is returned to indicate element is not present
A simple solution is to linearly search the given key in given array. Time complexity of this solution is O(n).
 We cab modify binary search to do it in O(Logn) time.

The idea is to compare the key with middle 3 elements, if present then return the index. If not present, then compare 
the key with middle element to decide whether to go in left half or right half. Comparing with middle element is enough 
as all the elements after mid+2 must be greater than element mid and all elements before mid-2 must be smaller than mid element.
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
