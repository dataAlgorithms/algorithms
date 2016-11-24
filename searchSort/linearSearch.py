'''
Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].
A simple approach is to do linear search, i.e
Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
If x matches with an element, return the index.
If x doesn’t match with any of elements, return -1.
'''
def linearSearch(theSeq, target):

    # get the length
    n = len(theSeq)

    # loop
    for pos in range(n):
        if target == theSeq[pos]:
            return pos
    else:
        return -1

'''
Result:

2
-1
-1
'''
if __name__ == "__main__":

    targets = [2, 6, None]
    theSeq = [1, 3, 2, 4, 5]
    for target in targets:
        print linearSearch(theSeq, target)
