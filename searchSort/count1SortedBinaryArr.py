'''
Method One, Simple

Count 1’s in a sorted binary array
Given a binary array sorted in non-increasing order, count the number of 1’s in it.
Examples:
Input: arr[] = {1, 1, 0, 0, 0, 0, 0}
Output: 2

Input: arr[] = {1, 1, 1, 1, 1, 1, 1}
Output: 7

Input: arr[] = {0, 0, 0, 0, 0, 0, 0}
Output: 0
A simple solution is to linearly traverse the array. The time complexity of the simple solution is O(n). 
'''

def count1BinaryArr(theSeq):

    # get the length
    n = len(theSeq)

    # do loop
    icount = 0
    for item in theSeq:
        if item == 1:
            icount += 1

    # print the count result
    print 'the number of 1 is ', icount

'''
the number of 1 is  2
the number of 1 is  7
the number of 1 is  0
'''
if __name__ == "__main__":
    for theSeq in [[1, 1, 0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1],
                   [0, 0, 0, 0, 0, 0, 0]]:
        count1BinaryArr(theSeq)
        
'''
Method Two: Optimize

Count 1’s in a sorted binary array
Given a binary array sorted in non-increasing order, count the number of 1’s in it.
Examples:
Input: arr[] = {1, 1, 0, 0, 0, 0, 0}
Output: 2

Input: arr[] = {1, 1, 1, 1, 1, 1, 1}
Output: 7

Input: arr[] = {0, 0, 0, 0, 0, 0, 0}
Output: 0

We can use Binary Search to find count in O(Logn) time. The idea is to look for last
 occurrence of 1 using Binary Search.
 Once we find the index last occurrence, we return index + 1 as count.
'''
def count1SortedArr(theSeq, low, high):

    while low <= high:
        mid = (low + high) // 2

        if (mid == high and theSeq[mid] == 1) or (theSeq[mid] == 1 and theSeq[mid+1] == 0):
            return mid+1
        if theSeq[mid] == 1:
            return count1SortedArr(theSeq, mid+1, high)
        else:
            return count1SortedArr(theSeq, low, mid-1)

    return 0

'''
2
7
0
'''
if __name__ == "__main__":
    for theSeq in [[1, 1, 0, 0, 0, 0, 0],
                   [1, 1, 1, 1, 1, 1, 1],
                   [0, 0, 0, 0, 0, 0, 0]]:
        print count1SortedArr(theSeq, 0, len(theSeq)-1)
