'''
Floor in a Sorted Array
Given a sorted array and a value x, the floor of x is the largest element
in array smaller than or equal to x. Write efficient functions to find floor of x.

Examples:

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 5
Output : 2
2 is the largest element in arr[] smaller than 5.

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 20
Output : 19
19 is the largest element in arr[] smaller than 20.

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 0
Output : -1
Since floor doesn't exist, output is -1.
'''

'''
Method 1 (Simple)

A simple solution is linearly traverse input sorted array and 
search for the first element greater than x. The element just before the found element is floor of x.
'''
def floorSearch(arr, x):

    # get the length
    n = len(arr)

    # if last element is smaller than x
    if x >= arr[n-1]:
        return n-1

    # if first element is greater than x
    if x < arr[0]:
        return -1

    # Linearly search for the first element
    # greater than x
    for i in range(1, n):
        if arr[i] > x:
            return i-1

    return -1

'''
floor of 7 is 6
floor of 5 is 2
floor of 20 is 19
floor of 0 doesnot exit in array
'''
if __name__ == "__main__":
    for arr,k in [[[-1, 2, 3, 5, 6, 8, 9, 10],7],
                  [[1, 2, 8, 10, 10, 12, 19],5],
                  [[1, 2, 8, 10, 10, 12, 19],20],
                  [[1, 2, 8, 10, 10, 12, 19],0]]:

        index = floorSearch(arr, k)
        if index == -1:
            print "floor of %d doesnot exit in array" % k
        else:
            print "floor of %d is %d" % (k, arr[index])
        
