def checkArrSort(A, n):

    if n == 1:
        return 1
   
    if A[n-1] < A[n-2]:
        return 0
    else:
        return checkArrSort(A, n-1)
        
'''
1
0
0
'''        
if __name__ == "__main__":
    A = [1, 2, 3, 4]
    print checkArrSort(A, len(A))

    A = [1, 23, 3, 4]
    print checkArrSort(A, len(A))

    A = [4, 3, 2, 1]
    print checkArrSort(A, len(A))
