1. binary search
def binarySearch(theSeq, theValue):

    theSeq = sorted(theSeq)

    n = len(theSeq)

    low = 0
    high = n -1
    while low <= high:
        mid = (low + high) // 2
        if theValue == theSeq[mid]:
            return True
        elif theValue > theSeq[mid]:
            low = mid+1
        else:
            high = mid-1

    return False

'''
True
True
True
False
'''
if __name__ == "__main__":
    theSeq = [1, 7, 3, 21, 0, 27, 25]

    for theValue in [7, 0, 25, 22]:
        print binarySearch(theSeq, theValue)
 
