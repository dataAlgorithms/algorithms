'''
1. count sort
'''
def countSort(theSeq):

    def countSortMain(A, k):
        n = len(A)

        B = []
        for i in range(n):
            B.append(0)

        C = []
        for i in range(k):
            C.append(0)

        for j in range(0, n):
            C[A[j]] = C[A[j]] + 1

        for i in range(1, k):
            C[i] = C[i] + C[i-1]

        for j in range(n-1, -1, -1): 
            B[C[A[j]]-1] = A[j]
            C[A[j]] = C[A[j]] - 1

        return B


    def diffMaxMin(A):

        small = A[0]
        large = A[0]
        for i in A:
            if i < small:
                small = i

            if i > large:
                large = i

        return large - small + 1


    k = diffMaxMin(theSeq)
    theSeq = countSortMain(theSeq, k)

    flag = 0
    for i in range(len(theSeq)):

        if theSeq[i] < 0:
            flag = 1
            break

    if flag == 1:
        newSeq = theSeq[:i]
        tmpSeq = theSeq[i:]

        tmpSeq.extend(newSeq)
    else:
        tmpSeq = theSeq 
        
    return tmpSeq

'''
theSeq sorted after: [-994, -943, -928, -873, -867, -811, -794, -779, -762, -730
, -668, -602, -581, -559, -513, -492, -470, -439, -430, -428, -414, -406, -403,
-372, -328, -284, -282, -197, -150, -90, -60, -35, 7, 38, 174, 177, 202, 262, 27
6, 302, 309, 333, 350, 445, 486, 510, 554, 559, 587, 616, 630, 661, 664, 746, 75
3, 761, 772, 799, 943, 962]
'''
if __name__ == "__main__":
    theSeq = [-994, -943, -928, -873, -867, -811, -794, -779, -762, -730, -668, -602, -581, -559, -513, -492, -470, -439, -430, -428, -414, -406, -403, -372, -328, -284, -282, -197, -150, -90, -60, -35, 7, 38, 174, 177, 202, 262, 276, 302, 309, 333, 350, 445, 486, 510, 554, 559, 587, 616, 630, 661, 664, 746, 753, 761, 772, 799, 943, 962]
    countSort(theSeq)
    print 'theSeq sorted after:', theSeq
