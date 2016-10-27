'''
5. Problem Statement: Given a sorted array with possible duplicate elements.
 Find number of occurrences of input key in log N time
'''
def getRightPosition(aList, l, r, key):

    while r -l > 1:
        m = (l+r) // 2
        if aList[m] <= key:
            l = m
        else:
            r = m

    return l

def getLeftPosition(aList, l, r, key):

    while r - l > 1:
        m = (l+r) // 2
        if aList[m] >= key:
            r = m
        else:
            l = m

    return r

def countOccurences(aList, key):
    left = getLeftPosition(aList, -1, len(aList)-1 , key)
    right = getRightPosition(aList, 0, len(aList), key)

    if aList[left] == key and key == aList[right]:
        return right - left + 1
    else:
        return 0

'''
2
0
1
'''
if __name__ == "__main__":
    aList = [-1, 2, 3, 5, 6, 6, 8, 9, 10]
    print countOccurences(aList, 6)
    print countOccurences(aList, 11)
    print countOccurences(aList, 2)
