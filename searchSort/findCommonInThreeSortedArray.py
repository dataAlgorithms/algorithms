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
