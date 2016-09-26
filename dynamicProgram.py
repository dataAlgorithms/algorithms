'''
1. Find minimum sum such that one of every three consecutive elements is taken
Given an array of n non-negative numbers, the task is to find the minimum sum of
 elements (picked from the array)
such that at least one element is picked out of every 3 consecutive elements in
the array.

Examples:

Input : arr[] = {1, 2, 3}
Output : 1

Input : arr[] = {1, 2, 3, 6, 7, 1}
Output : 4

1,2,3
2,3,6
3,6,7

6,7,1

3+1 = 4 (3 is in [1,2,3],[2,3,6],[3,7,7], 1 is in [6,7,1])

Input : arr[] = {1, 2, 3, 6, 7, 1, 8, 6, 2, 7, 7, 1}
Output: 7 (3+1+2+1=7)

1,2,3
2,3,6
3,6,7

6,7,1
7,1,8
1,8,6

8,6,2
6,2,7
2,7,7

7,7,1


Let sum(i) be the minimum possible sum when arr[i] is part of a solution sum (no
t necessarily result)
and is last picked element. Then our result is minimum of sum(n-1), sum(n-2) and
 sum(n-3)
[We must pick at least one of the last three elements].
We can recursively compute sum(i) as sum of arr[i] and minimum(sum(i-1), sum(i-2
), sum(i-3)).
Since there are overlapping subproblems in recursive structure of problem, we ca
n use Dynamic Programming to solve this problem.
'''

'''
Find minimum possible sum of elements of array
such that an element out of every three
consecutive is picked
'''

# A utility function to find minimum of 3 elements
def minimum(a, b, c):

    return min(min(a,b), c)

# Returns minimum possible sum of elements such
# that an element out of every three consecutive
# elements is picked
def findMinSum(arr):

    '''
    Create a DP table to store results of subpriblems. sum[i]
    is going to store minimum possible sum when arr[i] is
    part of the solution
    '''
    n = len(arr)

    theSum = [0] * n

    # when there are less than or equal to 3 elements
    theSum[0] = arr[0]
    theSum[1] = arr[1]
    theSum[2] = arr[2]

    # iterate through all other elements
    for i in range(3, n):
        theSum[i] = arr[i] + \
                      minimum(theSum[i-3], theSum[i-2], theSum[i-1])

    return minimum(theSum[n-1],theSum[n-2],theSum[n-3])

'''
1
4
7
4
'''
if __name__ == "__main__":
    for theSeq in [[1, 2, 3], [1, 2, 3, 6, 7, 1],
                   [1, 2, 3, 6, 7, 1, 8, 6, 2, 7, 7, 1],
                   [1, 2, 3, 20, 2, 10, 1]]:
        print findMinSum(theSeq)
