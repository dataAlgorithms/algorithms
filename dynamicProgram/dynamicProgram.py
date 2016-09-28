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

'''
2. Given a string, find count of distinct subsequences of it

Examples:

Input  : str = "gfg"
Output : 7
The seven distinct subsequences are "", "g", "f",
"gf", "fg", "gg" and "gfg"

Input  : str = "ggg"
Output : 4
The six distinct subsequences are "", "g", "gg"
and "ggg"

Let countSub(n) be count of subsequences of
first n characters in input string. We can
recursively write it as below.

countSub(n) = 2*Count(n-1) - Repetition

If current character, i.e., str[n-1] of str has
not appeared before, then
   Repetition = 0

Else:
   Repetition  =  Count(m)
   Here m is index of previous occurrence of
   current character. We basically remove all
   counts ending with previous occurrence of
   current character.

Since above recurrence has overlapping subproblems, 
we can solve it using Dynamic Programming
'''

MAX_CHAR = 256

# Returns count of distinct subsequence of str
def countSub(aStr):

    # Create an array to store index of last
    last = [-1] * MAX_CHAR

    # Length of string
    n = len(aStr)

    # dp[i] is going to store count of distinct
    # subsequences of length i
    dp = [0] * (n+1)

    # Empty substring has only one subsequence
    dp[0] = 1

    # Traverse through all lengths from 1 to n
    for i in range(1, n+1):
        # Number of subsequences with substring aStr[0..i-1]
        dp[i] = 2*dp[i-1]

        # If current character has appeared
        # before, then remove all subsequences
        # ending with previous occurrence
        if last[ord(aStr[i-1])] != -1:
            dp[i] = dp[i] - dp[last[ord(aStr[i-1])]]

        # Mark occurence of current character
        last[ord(aStr[i-1])] = i - 1

    return dp[n]

'''
7
4
2
128
496
'''
if __name__ == "__main__":
    for aStr in ["gfg", "ggg", "o", "ABCDEFG", "CODECRAFT"]:
        print countSub(aStr)

'''
3. Count digit groupings of a number with given constraints
We are given a string consisting of digits, we may group these digits into sub-groups
(but maintaining their original order). The task is to count number of groupings such that for every sub-group except the last one,
sum of digits in a sub-group is less than or equal to sum of the digits in the sub-group immediately on its right.

For example, a valid grouping of digits of number 1119 is (1-11-9). Sum of digits in first subgroup is 1, next subgroup is 2,
and last subgroup is 9. Sum of every subgroup is less than or equal to its immediate right.

Input : "1119"
Output: 7
Sub-groups: [1-119], [1-1-19], [1-11-9], [1-1-1-9],
            [11-19] and [111-9].
Note : Here we have included [1119] in the group and
       sum of digits is 12 and this group has no
       immediate right.

Input : "1234"
Output: 6
Sub-groups : [1234], [1-234], [12-34], [1-2-3-4],
             [12-3-4] and [1-2-34]

The maximum sum of digits can be 9*length where ‘length’ is length of input num.
Create a 2D array int dp[MAX][9*MAX] where MAX is maximum possible length of input numebr.
A value dp[position][previous] is going to store result for ‘position’ and ‘previous_sum’.
If current subproblem has been evaluated i.e; dp[position][previous_sum] != -1,
then use this result, else recursively compute its value.
If by including the current position digit in sum i.e; sum = sum + num[position]-‘0′,
sum becomes greater than equal to previous sum, then increment the result and call the problem for next position in the num.
If position == length, then we have been traversed current subgroup successfully and we return 1;
'''

MAX = 40

# Function to find the count of splits with given condition
def countGroups(position, previous_sum, length, numList):

    # Terminating condition
    if position == length:
        return 1

    # If already evaluated for a given sub problem then return the value
    if dp[position][previous_sum] != -1:
        return dp[position][previous_sum]

    # countGroups for current sub-group is 0
    dp[position][previous_sum] = 0

    res = 0
    theSum = 0

    # traverse all digits from current position to rest
    # of the length of string
    for i in range(position, length):
        theSum += int(numList[i]) 

        # if forward_sum is greater than the previous sum
        # then call the method again
        if theSum >= previous_sum:
            # note: we pass current sum as previous sum
            res += countGroups(i+1, theSum, length, numList)

    dp[position][previous_sum] = res

    # total number of subgroups till current position
    return res

'''
7
6
'''
if __name__ == "__main__":
    for numList in ["1119", "1234"]:
        length = len(numList)

        # A memoization table to store results of subproblems
        # length of string is 40 and maximum sum will be 9*40
        dp = [[-1] * (9*MAX+1) for _ in range(MAX)]

        print countGroups(0, 0, length, numList)
