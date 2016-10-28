'''
Search an element in an array where difference between adjacent elements is 1
Given an array where difference between adjacent elements is 1, 
write an algorithm to search for an element in the array and 
return the position of the element (return the first occurrence).

Examples:

Let element to be searched be x

Input: arr[] = {8, 7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3}
       x = 3
Output: Element 3 found at index 7

Input: arr[] =  {1, 2, 3, 4, 5, 4}
       x = 5
Output: Element 5 found at index 4

The above solution can be Optimized using the fact that difference between all adjacent elements is 1. 
The idea is to start comparing from the leftmost element and find the difference between current array 
element and x. Let this difference be ‘diff’. From the given property of array, we always know that x 
must be at-least ‘diff’ away, so instead of searching one by one, we jump ‘diff’. 
'''
def adjacentSearch(arr, x):

    # get the length
    n = len(arr)

    # Travers the given array starting from
    # leftmost element
    i = 0
    while i < n:
        # if x is found at index i
        if arr[i] == x:
            return i

        # jump the difference between current
        # array element and x
        i = i + abs(arr[i]-x)

    return -1

'''
7
3
'''
if __name__ == "__main__":
    arr = [8 ,7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3]
    x = 3
    print adjacentSearch(arr, x)

    arr = [1, 2, 3, 4, 5, 4]
    x = 4
    print adjacentSearch(arr, x)
