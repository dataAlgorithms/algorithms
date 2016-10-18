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

'''
[-1, 2, 3, 5, 7]
'''
if __name__ == "__main__":
    theSeq = [2, -1, 3, 5, 7]
    selectSort(theSeq)
    print theSeq
