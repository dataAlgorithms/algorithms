'''
Method 1: Simple Way
Find common elements in three sorted arrays

Examples:

ar1[] = {1, 5, 10, 20, 40, 80}
ar2[] = {6, 7, 20, 80, 100}
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20, 80

ar1[] = {1, 5, 5}
ar2[] = {3, 4, 5, 5, 10}
ar3[] = {5, 5, 10, 20}
Output: 5, 5

A simple solution is to first find intersection of two arrays and store the intersection in a temporary array, 
then find the intersection of third array and temporary array. Time complexity of this solution is O(n1 + n2 + n3) 
where n1, n2 and n3 are sizes of ar1[], ar2[] and ar3[] respectively.
'''
def findCommonSimple(ar1, ar2, ar3):

    # get the length
    n1 = len(ar1)
    n2 = len(ar2)
    n3 = len(ar3)

    # do loop
    ar = []
    for item in ar2:
        if item in ar1:
            ar.append(item)

    theAr = []
    for item in ar:
        if item in ar3:
            theAr.append(item)

    print theAr

'''
[20, 80]
[5, 5]
[20, 80]
'''
if __name__ == "__main__":
    ar1 = [1, 5, 10, 20, 40, 80]
    ar2 = [6, 7, 20, 80, 100]
    ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
    findCommonSimple(ar1, ar2, ar3)

    ar1 = [1, 5, 5]
    ar2 = [3, 4, 5, 5, 10]
    ar3 = [5, 5, 10, 20]
    findCommonSimple(ar1, ar2, ar3)

    ar1 = [1, 5, 10, 20, 40, 80]
    ar2 = [6, 7, 20, 80, 100]
    ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
    findCommonSimple(ar1, ar2, ar3)

'''
Method Two: Optimize Way

Find common elements in three sorted arrays
Given three arrays sorted in non-decreasing order, print all common elements in these arrays.

Examples:

ar1[] = {1, 5, 10, 20, 40, 80}
ar2[] = {6, 7, 20, 80, 100}
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20, 80

ar1[] = {1, 5, 5}
ar2[] = {3, 4, 5, 5, 10}
ar3[] = {5, 5, 10, 20}
Output: 5, 5

Let the current element traversed in ar1[] be x, in ar2[] be y and in ar3[] be z. 
We can have following cases inside the loop.
1) If x, y and z are same, we can simply print any of them as common element and move ahead in all three arrays.
2) Else If x < y, we can move ahead in ar1[] as x cannot be a common element 
3) Else If y < z, we can move ahead in ar2[] as y cannot be a common element 
4) Else (We reach here when x > y and y > z), we can simply move ahead in ar3[] as z cannot be a common element.

Time complexity of the above solution is O(n1 + n2 + n3)
'''
def findCommon(ar1, ar2, ar3):

    # get the length
    n1 = len(ar1)
    n2 = len(ar2)
    n3 = len(ar3)

    # set the primary index
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2 and k < n3:
        # if three are equal
        if ar1[i] == ar2[j] == ar3[k]:
            print ar1[i],
            i += 1
            j += 1
            k += 1
        elif ar1[i] < ar2[j]:
            i += 1
        elif ar2[j] < ar3[k]:
            j += 1
        else:
            k += 1
    print ''

'''
20 80
5 5
20 80
'''
if __name__ == "__main__":
    ar1 = [1, 5, 10, 20, 40, 80]
    ar2 = [6, 7, 20, 80, 100]
    ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
    findCommon(ar1, ar2, ar3)

    ar1 = [1, 5, 5]
    ar2 = [3, 4, 5, 5, 10]
    ar3 = [5, 5, 10, 20]
    findCommon(ar1, ar2, ar3)

    ar1 = [1, 5, 10, 20, 40, 80]
    ar2 = [6, 7, 20, 80, 100]
    ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
    findCommon(ar1, ar2, ar3)
