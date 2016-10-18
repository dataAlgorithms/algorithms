def selectSort(theSeq):

    n = len(theSeq)
    for i in range(n-1):
        smallNdx = i
        for j in range(i+1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j

        if smallNdx != i:
            tmp = theSeq[smallNdx]
            theSeq[smallNdx] = theSeq[i]
            theSeq[i] = tmp
