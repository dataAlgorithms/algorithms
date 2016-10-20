'''
Sort an array in wave
This can be done in O(n) time by doing a single traversal of given array. The idea is based on the 
fact that if we make sure that all even positioned (at index 0, 2, 4, ..) elements are greater than their 
adjacent odd elements, we don’t need to worry about odd positioned element. Following are simple steps.
1) Traverse all even positioned elements of input array, and do following.
….a) If current element is smaller than previous odd element, swap previous and current.
….b) If current element is smaller than next odd element, swap next and current.

Below are implementations of above simple algorithm.

C++PythonJava
# Python function to sort the array arr[0..n-1] in wave form,
# i.e., arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= arr[5]
'''
def sortInWave(arr):

    # Get the length
    n = len(arr)

    # Traverse all even elements
    for i in range(0, n, 2):

        # If current even element is smaller than previous
        if i > 0 and arr[i] < arr[i-1]:
            arr[i],arr[i-1] = arr[i-1],arr[i]

        # If current even element is smaller than next
        if i < n-1 and arr[i] < arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]

'''
[90, 10, 49, 1, 5, 2, 23]
[10, 5, 6, 2, 20, 3, 100, 80]
[20, 8, 10, 4, 6, 2]
[4, 2, 8, 6, 20, 10]
[6, 3, 10, 5, 20, 7]
'''
if __name__ == "__main__":
    for arr in [[10, 90, 49, 2, 1, 5, 23], [10, 5, 6, 3, 2, 20, 100, 80], 
                    [20, 10, 8, 6, 4, 2], [2, 4, 6, 8, 10, 20],
                    [3, 6, 5, 10, 7, 20]]:
        sortInWave(arr)
        print arr
