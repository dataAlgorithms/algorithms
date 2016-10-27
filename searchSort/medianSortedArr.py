'''
1. Median of two sorted arrays
'''

# Simply count while merging
'''
Use merge procedure of merge sort. Keep track of count while comparing elements of two arrays. If count becomes n(For 2n elements), we have reached the median. Take the average of the elements at indexes n-1 and n in the merged array
'''
def simpleGetMedian(ar1, ar2):

    n = len(ar1)
    i = 0
    j = 0
    m1 = -1
    m2 = -1

    '''
    Since there are 2n elements, median will be average
    of elements at index n-1 and n in the array obtained after
     merging ar1 and ar2
    '''
    for count in range(n+1):
        '''
        Below is to handle case where all elements of ar1[] are
        smaller than smallest(or first) element of ar2[]
        '''
        if i == n:
            m1 = m2
            m2 = ar2[0]
            break

        elif j == n:
            '''
            Below is to handle case where all elements of ar2[] are
            smaller than smallest(or first) element of ar1[]
            '''
            m1 = m2
            m2 = ar1[0]
            break

        if ar1[i] < ar2[j]:
            m1 = m2
            m2 = ar1[i]
            i += 1
        else:
            m1 = m2
            m2 = ar2[j]
            j += 1

    return (m1 + m2) * 0.5


'''
find median sorted array using binary search
'''
def getMedianDC(A, B):

    def findKth(A, B, k, aStart, aEnd, bStart, bEnd):
        aLen = aEnd - aStart + 1
        bLen = bEnd - bStart + 1

        # Handle special cases
        if aLen == 0:
            return B[bStart + k]
        if bLen == 0:
            return A[aStart + k]
        if k == 0:
            if A[aStart] < B[bStart]:
                return A[aStart]
            else:
                return B[bStart]

        aMid = aLen * k / (aLen + bLen)
        bMid = k - aMid - 1

        aMid = aMid + aStart
        bMid = bMid + bStart

        if A[aMid] > B[bMid]:
            k = k - (bMid - bStart + 1)
            aEnd = aMid
            bStart = bMid + 1
        else:
            k = k - (aMid - aStart + 1)
            bEnd = bMid
            aStart = aMid + 1

        return findKth(A, B, k, aStart, aEnd, bStart, bEnd)
    m = len(A)
    n = len(B)

    if (m+n)%2 != 0:
        return findKth(A, B, (m+n)/2, 0, m-1, 0, n-1)
    else:
        return (findKth(A, B, (m+n)/2, 0, m-1, 0, n-1) + \
                findKth(A, B, (m+n)/2-1, 0, m-1, 0, n-1)) * 0.5

'''
16.0
16.0
2.5
2.5
'''
if __name__ == "__main__":
    ar1 = [1, 12, 15, 26, 38]
    ar2 = [2, 13, 17, 30, 45]
    print simpleGetMedian(ar1, ar2)
    print getMedianDC(ar1, ar2)
    ar1 = [1, 2]
    ar2 = [3, 4]
    print simpleGetMedian(ar1, ar2)
    print getMedianDC(ar1, ar2)
