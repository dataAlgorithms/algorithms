'''
Find the element before which all the elements are smaller than it,
and after which all are greater
Given an array, find an element before which all elements are smaller than it,
and after which all are greater than it. Return index of the element if
there is such an element, otherwise return -1.

Examples:

Input:   arr[] = {5, 1, 4, 3, 6, 8, 10, 7, 9};
Output:  Index of element is 4
All elements on left of arr[4] are smaller than it
and all elements on right are greater.

Input:   arr[] = {5, 1, 4, 4};
Output:  Index of element is -1
Expected time complexity is O(n).

A Simple Solution is to consider every element one by one.
For every element, compare it with all elements on left and all elements on right.
Time complexity of this solution is O(n2).

An Efficient Solution can solve this problem in O(n) time 
using O(n) extra space. Below is detailed solution.

1) Create two arrays leftMax[] and rightMin[].
2) Traverse input array from left to right and fill leftMax[] such that leftMax[i] 
contains maximum element from 0 to i-1 in input array.
3) Traverse input array from right to left and fill rightMin[] such that rightMin[i] 
contains minimum element from to n-1 to i+1 in input array.
4) Traverse input array. For every element arr[i], check if arr[i] is greater 
than leftMax[i] and smaller than rightMin[i]. If yes, return i.

Further Optimization to above approach is to use only one extra array and traverse 
input array only twice. First traversal is same as above and fills leftMax[]. 
Next traversal traverses from right and keeps track of minimum. 
The second traversal also finds the required element.
'''
def findElement(arr):

    # import 
    import sys

    # get the length
    n = len(arr)

    # leftMax[i] stores maximum of arr[0..i-1]
    leftMax = [0] * n
    leftMax[0] = -1

    # fill leftMax[1..n-1]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], arr[i-1])

    # initialize minimum from right
    rightMin = sys.maxint

    # traverse array from right
    for i in range(n-1, -1, -1):
        # check if we found a required element
        if leftMax[i] < arr[i] and rightMin > arr[i]:
            return arr[i]

        # update right minimum
        rightMin = min(rightMin, arr[i])

    return -1

'''
6
-1
'''
if __name__ == "__main__":
    arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    print findElement(arr)

    arr = [5, 1, 4, 4]
    print findElement(arr)
