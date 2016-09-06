def newrange(stop):
   i = 0
   while i < stop:
       yield i
       i += 1

def binarySearchIter(theSeq, target):

    # get the length of theSeq
    n = len(theSeq)

    # loop
    low = 0
    high = n - 1
    while low <= high:
        mid = (low+high) // 2
        if target == theSeq[mid]:
            return mid
        elif target < theSeq[mid]:
            high = mid-1
        else:
            low = mid+1

    return -1

def binarySearchRec(theSeq, left, right, target):


    if left <= right:
        mid = (left + right) // 2
        if target == theSeq[mid]:
            return mid
        elif target < theSeq[mid]:
            return binarySearchRec(theSeq, left, mid-1, target)
        else:
            return binarySearchRec(theSeq, mid+1, right, target)

    return -1


if __name__ == "__main__":
    theSeq = [i for i in newrange(10000000)]
    target = 50
    print binarySearchIter(theSeq, target)  
    print binarySearchRec(theSeq, 0, len(theSeq)-1, target)  
