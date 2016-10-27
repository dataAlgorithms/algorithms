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
