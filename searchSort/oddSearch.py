'''
Find the odd appearing element in O(Log n) time
Given an array where all elements appear
even number of times except one.
All repeating occurrences of elements appear in pairs and these
pairs are not adjacent (there cannot be more than two consecutive
occurrences of any element). Find the element that appears odd number of times.

Note that input like {2, 2, 1, 2, 2, 1, 1} is valid as all repeating occurrences
occur in pairs and these pairs are not adjacent. Input like {2, 1, 2} is invalid as
repeating elements don’t appear in pairs. Also, input like {1, 2, 2, 2, 2} is
invalid as two pairs of 2 are adjacent. Input like {2, 2, 2, 1} is also invalid
as there are three consecutive occurrences of 2.

Example:

Input: arr[] = {1, 1, 2, 2, 1, 1, 2, 2, 13, 1, 1, 40, 40, 13, 13}
Output: 13

Input: arr[] = {1, 1, 2, 2, 3, 3, 4, 4, 3, 600, 600, 4, 4}
Output: 3

A Better Solution is to do XOR of all elements, result of XOR would 
give the odd appearing element. Time complexity of this solution is O(n). 

An Efficient Solution can find the required element in O(Log n) time. 
The idea is to use Binary Search. Below is an observation in input array.
Since the element appears odd number of times, there must be a single 
occurrence of the element. For example, in {2, 1, 1, 2, 2), the first 2 
is the odd occurrence. So the idea is to find this odd occurrence using Binary Search.
All elements before the odd occurrence have first occurrence at even index (0, 2, ..) 
and next occurrence at odd index (1, 3, …). And all elements afterhave first 
occurrence at odd index and next occurrence at even index.

1) Find the middle index, say ‘mid’.
2) If ‘mid’ is even, then compare arr[mid] and arr[mid + 1]. 
If both are same, then there is an odd occurrence of the element after ‘mid’ else before mid.
3) If ‘mid’ is odd, then compare arr[mid] and arr[mid – 1]. If both are same, 
then there is an odd occurrence after ‘mid’ else before mid.
'''
def oddSearch(arr, low, high):

    # Base case 
    if low > high:
        return -1
    if low == high:
        return arr[low]

    # find the middle point
    mid = (low + high) // 2

    # if mid is even
    if mid%2 == 0:
        # If the element next to mid is same as mid
        # then output elemnet lies on right side
        # else on left side
        if arr[mid] == arr[mid+1]:
            return oddSearch(arr, mid+2, high)
        else:
            return oddSearch(arr, low, mid)

    else:
        # else if mid is odd
        if arr[mid] == arr[mid-1]:
            return oddSearch(arr, mid+1, high)
        else:
            # (mid-1) because target element can only exit at even place
            return oddSearch(arr, low, mid-1)

    return -1

'''
13
3
'''
if __name__ == "__main__":
    arr = [ 1, 1, 2, 2, 1, 1, 2, 2, 13, 1, 1, 40, 40 ]
    print oddSearch(arr, 0, len(arr)-1 )

    arr = [1, 1, 2, 2, 3, 3, 4, 4, 3, 600, 600, 4, 4]
    print oddSearch(arr, 0, len(arr)-1 )
