'''
Third largest element in an array of distinct elements
Given an array of distinct elements, find third largest element in it.

Example :

Input  : arr[] = {1, 14, 2, 16, 10, 20}
Output : The third Largest element is 14

Input  : arr[] = {19, -10, 20, 14, 2, 16, 10}
Output : The third Largest element is 16
We strongly recommend that you click here and practice it, before moving on to the solution.

Method 1 (Simple) Simplest way to solve this question is to first iterate through 
the array and find first maximum. Store this first maximum as well as its index. 
Now traverse the whole array finding the second max with the changed condition. 
Finally traverse the array third time and find the third largest element.
'''
def thirdLargest(arr):

    # get the length
    n = len(arr)

    # there should be at least three elements
    if n < 3:
        print "Array should at least have 3 elements."
        return

    # find first largest element
    first = arr[0]
    for i in range(1, n):
        if arr[i] > first:
            first = arr[i]

    # find second largest element
    second = -1
    for i in range(0, n):
        if arr[i] > second and arr[i] < first:
            second = arr[i]

    # find third largest element
    third = -1
    for i in range(0, n):
        if arr[i] > third and arr[i] < second:
            third = arr[i]

    print "the third largest element is ", third

if __name__ == "__main__":
    arr = [12, 13, 1, 10, 34, 16]
    thirdLargest(arr)

 
