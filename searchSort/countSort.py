'''
1. count sort

Counting sort is a sorting technique based on keys between a specific range.
It works by counting the number of objects having distinct key values (kind of hashing). 
Then doing some arithmetic to calculate the position of each object in the output sequence.

Let us understand it with the help of an example.

For simplicity, consider the data in the range 0 to 9.
Input data: 1, 4, 1, 2, 7, 5, 2
  1) Take a count array to store the count of each unique object.
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  2  0   1  1  0  1  0  0

  2) Modify the count array such that each element at each index
  stores the sum of previous counts.
  Index:     0  1  2  3  4  5  6  7  8  9
  Count:     0  2  4  4  5  6  6  7  7  7

The modified count array indicates the position of each object in
the output sequence.
 
  3) Output each object from the input sequence followed by
  decreasing its count by 1.
  Process the input data: 1, 4, 1, 2, 7, 5, 2. Position of 1 is 2.
  Put data 1 at index 2 in output. Decrease count by 1 to place
  next data 1 at an index 1 smaller than this index.
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
