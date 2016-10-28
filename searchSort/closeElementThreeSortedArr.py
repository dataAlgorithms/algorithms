'''
Find three closest elements from given three sorted arrays
Given three sorted arrays A[], B[] and C[], find 3 elements i, j and k
from A, B and C respectively such that max(abs(A[i] – B[j]),
abs(B[j] – C[k]), abs(C[k] – A[i])) is minimized. Here abs() indicates absolute value.

Example :

Input: A[] = {1, 4, 10}
       B[] = {2, 15, 20}
       C[] = {10, 12}
Output: 10 15 10
10 from A, 15 from B and 10 from C

Input: A[] = {20, 24, 100}
       B[] = {2, 19, 22, 79, 800}
       C[] = {10, 12, 23, 24, 119}
Output: 24 22 23
24 from A, 22 from B and 23 from C

A Simple Solution is to run three nested loops to
consider all triplets from A, B and C. Compute the value of
max(abs(A[i] – B[j]), abs(B[j] – C[k]), abs(C[k] – A[i])) for
every triplet and return minimum of all values. Time complexity of this solution is O(n3)

A Better Solution is to us Binary Search.
1) Iterate over all elements of A[],
      a) Binary search for element just smaller than or equal to in B[] and C[], and note the difference.
2) Repeat step 1 for B[] and C[].
3) Return overall minimum.

Time complexity of this solution is O(nLogn)

Efficient Solution Let ‘p’ be size of A[], ‘q’ be size of B[] and ‘r’ be size of C[]

1)   Start with i=0, j=0 and k=0 (Three index variables for A,
                                  B and C respectively)

//  p, q and r are sizes of A[], B[] and C[] respectively.
2)   Do following while i < p and j < q and k < r
    a) Find min and maximum of A[i], B[j] and C[k]
    b) Compute diff = max(X, Y, Z) - min(A[i], B[j], C[k]).
    c) If new result is less than current result, change
       it to the new result.
    d) Increment the pointer of the array which contains
       the minimum.
Note that we increment the pointer of the array which has the minimum, because our goal is to decrease the difference. 
Increasing the maximum pointer increases the difference. 
Increase the second maximum pointer can potentially increase the difference.
'''
def findClosest(A, B, C):

    # import 
    import sys

    # get the length
    p = len(A)
    q = len(B)
    r = len(C)

    # initialize min diff
    diff = sys.maxint

    # initialize result
    res_i = 0
    res_j = 0
    res_k = 0

    # traverse array
    i = 0
    j = 0
    k = 0
    while i < p and j < q and k < r:
        # find minimum and maximum of current three elements
        themin = min(A[i],min(B[j],C[k]))
        themax = max(A[i],max(B[j],C[k]))

        # update result if current diff is less than the min
        # diff so far
        if themax - themin < diff:
            res_i = i
            res_j = j
            res_k = k
            diff = themax - themin

        # we cannot get less than 0 as values are absolute
        if diff == 0:
            break

        # increment index of array with smallest value
        if A[i] == themin:
            i += 1
        elif B[j] == themin:
            j += 1
        else:
            k += 1

    print A[res_i],B[res_j],C[res_k]

'''
10 15 10
24 22 23
'''
if __name__ == "__main__":
    A = [1, 4, 10]
    B = [2, 15, 20]
    C = [10, 12]
    findClosest(A, B, C)

    A = [20, 24, 100]
    B = [2, 19, 22, 79, 800]
    C = [10, 12, 23, 24, 119]
    findClosest(A, B, C)
