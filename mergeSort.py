'''
1. Merge sort
  use divide and conquer way to sort
'''
def mergeSort(theSeq):

    # get the length 
    n = len(theSeq)

    # tmpList to store the item
    tmpList = [0] * n

    # rec merge sort
    recMergeSort(theSeq, 0, n-1, tmpList)

def recMergeSort(theSeq, first, last, tmpList):

    if first == last:
        return
    else:
        mid = (first + last) // 2
        recMergeSort(theSeq, first, mid, tmpList)
        recMergeSort(theSeq, mid+1, last, tmpList)

        mergeVitualSeq(theSeq, first, mid+1, last+1, tmpList)

def mergeVitualSeq(theSeq, left, right, end, tmpList):

    a = left
    b = right
    m = 0
    while a < right and b < end:
        if theSeq[a] < theSeq[b]:
            tmpList[m] = theSeq[a]
            m += 1
            a += 1
        else:
            tmpList[m] = theSeq[b]
            m += 1
            b += 1

    while a < right:
        tmpList[m] = theSeq[a]
        m += 1
        a += 1

    while b < end:
        tmpList[m] = theSeq[b]
        m += 1
        b += 1

    for i in range(end-left):
        theSeq[left+i] = tmpList[i]

def test_mergeSort():
    
    # do the linear search
    theValues = [35, -85, -92, -52, -496, 216, -860, 435, -976, -966, -919, 950, 605, -547, 537, -311, -20, 53, 856, 50, -210, 580, -979, 912, 275, -701, -800, -953, -2, -769, 572, 509, 723, -490, -957, -341, -899, 263, -109, -895, 989, 345, -282, 547, -678, -304, -998, 610, 478, -333, -783, -915, -454, -665, 729, -303, 78, 652, 228, 394]
    mergeSort(theValues)
    
    print theValues
        
'''
[-998, -979, -976, -966, -957, -953, -919, -915, -899, -895, -860, -800, -783, -769, -701, -678, -665, -547, -496, -490, -454, -341, -333, -311, -304, -303, -282, -210, -109, -92, -85, -52, -20, -2, 35, 50, 53, 78, 216, 228, 263, 275, 345, 394, 435, 478, 509, 537, 547, 572, 580, 605, 610, 652, 723, 729, 856, 912, 950, 989]
'''
if __name__ == "__main__":
    test_mergeSort()
