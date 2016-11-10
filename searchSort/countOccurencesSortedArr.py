#! coding=utf-8

'''
Problem Statement: Given a sorted array with possible duplicate elements.
Find number of occurrences of input key in log N time.

The idea here is finding left and right most occurrences of key in the array using binary search. 
We can modify floor function to trace right most occurrence and left most occurrence. 
'''
def occurenceCount(theSeq, target):

    '''
    Input: Indices ragne [l...r)
    Invariant: theSeq[l] <= target and theSeq[r] > target
    '''
    def getRightPosition(theSeq, l, r, target):
        
        while r-l > 1:
            m = l + (r -l)/2

            if theSeq[m] <= target:
                l = m
            else:
                r = m

        return l

    '''
    Input: Indices Range (l...r]
    Invariant: theSeq[r] >= target and theSeq[l] > target
    '''
    def getLeftPosition(theSeq, l, r, target):
        
        while r-l > 1:
            m = l + (r-l) /2
          
            if theSeq[m] >= target:
                r = m
            else:
                l = m

        return r

    # observe boundary conditions
    left = getLeftPosition(theSeq, -1, len(theSeq)-1, target)
    right = getRightPosition(theSeq, 0, len(theSeq), target)

    # what if the element doesnot exists in the array
    # the checks helps to trace that element exists
    if theSeq[left] == target and target == theSeq[right]:
        return right-left+1
    else:
        return 0

'''
2
0
1
'''
if __name__ == "__main__":
    aList = [-1, 2, 3, 5, 6, 6, 8, 9, 10]
    print occurenceCount(aList, 6)
    print occurenceCount(aList, 11)
    print occurenceCount(aList, 2)
