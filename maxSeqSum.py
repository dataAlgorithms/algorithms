# get random numbers
def getRandomNum(num=6):

    import random

    lottery_numbers = range(-1000, 1000)
    
    winning_numbers = random.sample(lottery_numbers, num)
    
    print winning_numbers
    return winning_numbers

# Find max sum array using brute-force
def maxSubSeqBf(aList=None):

    if aList is None:
        return

    n = len(aList)
    maxSum = 0
    for i in range(n):
        theSum = 0
        for j in range(i,n):
            theSum += aList[j]
            if theSum > maxSum:
                maxSum = theSum
                left = i
                right = j

    print maxSum, left, right
    
# Find the max sum array using recursive 
def maxSumSeqRec(aList, left, right):

    if left == right:
        if left > 0:
            return aList[left]
        else:
            return 0

    mid = (left+right) // 2
    maxSumLeft = maxSumSeqRec(aList, left, mid)
    maxSumRight = maxSumSeqRec(aList, mid+1, right)

    sumLeft = 0
    leftSum = 0
    for i in range(mid, left-1, -1):
        leftSum += aList[i]
        if leftSum > sumLeft:
            sumLeft = leftSum

    sumRight = 0
    rightSum = 0
    for j in range(mid+1, right+1):
        rightSum += aList[j]
        if rightSum > sumRight:
            sumRight = rightSum


    tmpSum = max(maxSumLeft,maxSumRight)
    theSum = sumLeft + sumRight
    return max(tmpSum, theSum)

def maxSumSeqRecMain(aList):

    n = len(aList)
    print maxSumSeqRec(aList, 0, n-1)

# Find the max sum array using dynamic programming
def maxSumSeqDp(aList):

    maxSum = 0
    theSum = 0
    for i in aList:
        theSum += i
        if maxSum < theSum:
            maxSum = theSum
        elif theSum < 0:
            theSum = 0

    print maxSum
    return maxSum

if __name__ == "__main__":
    aList = getRandomNum()
    oneList = aList
    otherList = aList
    maxSubSeqBf(oneList)
    maxSumSeqRecMain(otherList)
    maxSumSeqDp(aList)
