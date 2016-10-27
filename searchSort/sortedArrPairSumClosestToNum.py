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
