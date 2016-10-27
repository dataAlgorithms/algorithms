'''
Method One, Simple Way

Given a sorted array and a number x, find the pair in array whose sum is closest to x

Examples:
Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10

A simple solution is to consider every pair and keep track of closest pair 
(absolute difference between pair sum and x is minimum). 

Time complexity of this solution is O(n2)
'''
def sortedArrPairSumClosestToNum(theSeq, x):

    # import lib
    import sys

    # get the length
    n = len(theSeq)

    # set mimimum
    themin = sys.maxint
    imin = 0
    jmin = 0

    # do loop
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(theSeq[i] + theSeq[j] - x) < themin:
                themin = abs(theSeq[i] + theSeq[j] - x)
                imin = i
                jmin = j

    print theSeq[imin], theSeq[jmin], theSeq[imin]+theSeq[jmin]

'''
22 30 52
4 10 14
'''
if __name__ == "__main__":
    theSeq = [10, 22, 28, 29, 30, 40]    
    x = 54
    sortedArrPairSumClosestToNum(theSeq, x)    

    theSeq = [1, 3, 4, 7, 10]
    x = 15
    sortedArrPairSumClosestToNum(theSeq, x)    
    
'''
Method Two: Optimize

Given a sorted array and a number x, find a pair in array whose sum is closest to x.
Examples:
Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10

An efficient solution can find the pair in O(n) time. 
Following is detailed algorithm.
1) Initialize a variable diff as infinite (Diff is used to store the 
   difference between pair and x).  We need to find the minimum diff.
2) Initialize two index variables l and r in the given sorted array.
       (a) Initialize first to the leftmost index:  l = 0
       (b) Initialize second  the rightmost index:  r = n-1
3) Loop while l < r.
       (a) If  abs(arr[l] + arr[r] - sum) < diff  then 
           update diff and result 
       (b) Else if(arr[l] + arr[r] <  sum )  then l++
       (c) Else r--    
'''

def sortedArrPairSumClosestToNum(theSeq, x):

    # import lib
    import sys

    # get the length
    n = len(theSeq)

    # do loop
    left = 0
    right = n - 1
    diff = sys.maxint

    while left < right:
        if abs(theSeq[left] + theSeq[right] - x) < diff:
            lmin = left
            rmin = right
            diff = abs(theSeq[left] + theSeq[right] -x)
 
        if theSeq[left] + theSeq[right] > x:
            right -= 1
        else:
            left += 1

    print theSeq[lmin], theSeq[rmin], theSeq[lmin]+theSeq[rmin]

'''
22 30 52
4 10 14
'''
if __name__ == "__main__":
    theSeq = [10, 22, 28, 29, 30, 40]    
    x = 54
    sortedArrPairSumClosestToNum(theSeq, x)    

    theSeq = [1, 3, 4, 7, 10]
    x = 15
    sortedArrPairSumClosestToNum(theSeq, x)    
