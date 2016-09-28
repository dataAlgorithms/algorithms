'''
Let us discuss Longest Increasing Subsequence (LIS) problem as an example problem that can be solved using Dynamic Programming.
The longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence
such that all elements of the subsequence are sorted in increasing order. For example,
length of LIS for { 10, 22, 9, 33, 21, 50, 41, 60, 80 } is 6 and LIS is {10, 22, 33, 50, 60, 80}.

We strongly recommend that you click here and practice it, before moving on to the solution.

Optimal Substructure:
Let arr[0..n-1] be the input array and L(i) be the length of the LIS till index i
such that arr[i] is part of LIS and arr[i] is the last element in LIS, then L(i) can be recursively written as.
L(i) = { 1 + Max ( L(j) ) } where j < i and arr[j] < arr[i] and if there is no such j then L(i) = 1
To get LIS of a given array, we need to return max(L(i)) where 0 < i < n So the LIS problem
has optimal substructure property as the main problem can be solved using solutions to subproblems.
'''

# longest increasing subsequence
def longIncSub(arr):

    n = len(arr)
    tmpList = []

    # Declare the list (array( for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n

    # Compute optimized LIS values in bootom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Initialize maximum to 0 to get the maximum of all LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        if lis[i] > maximum:
            maximum = lis[i]
            tmpList.append(arr[i])

    return maximum, tmpList

'''
(5, [10, 22, 33, 50, 60])
'''
if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print longIncSub(arr)
