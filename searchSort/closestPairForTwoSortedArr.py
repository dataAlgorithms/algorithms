'''
Method 1: Simple Solution
Find the closest pair from two sorted arrays
Given two sorted arrays and a number x, 
find the pair whose sum is closest to x and 
the pair has an element from each array.
'''
def closestPairForTwoSortedArr(ar1, ar2, x):

    n1 = len(ar1)
    n2 = len(ar2)

    i_min = 0
    j_min = 0
    v_min = ar1[i_min],ar2[j_min]

    for i in range(n1):
        for j in range(n2):
            if abs(ar1[i] + ar2[j] - x) < v_min:
                v_min = abs(ar1[i] + ar2[j]-x)
                i_min = i
                j_min = j

    print ar1[i_min], ar2[j_min], ar1[i_min] + ar2[j_min]

'''
1 30 31
7 40 47
'''
if __name__ == "__main__":
    ar1 = [1, 4, 5, 7]
    ar2 = [10, 20, 30, 40]
    x = 32
    closestPairForTwoSortedArr(ar1, ar2, x)

    ar1 = [1, 4, 5, 7]
    ar2 = [10, 20, 30, 40]
    x = 50
    closestPairForTwoSortedArr(ar1, ar2, x)
    
    
