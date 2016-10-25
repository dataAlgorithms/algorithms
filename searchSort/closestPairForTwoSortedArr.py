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
    
'''
Method 2: MergeWay

1) Merge given two arrays into an auxiliary array of size m+n using merge process of merge sort. 
While merging keep another boolean array of size m+n to indicate whether the current element in 
merged array is from ar1[] or ar2[].

2) Consider the merged array and use the linear time algorithm to 
find the pair with sum closest to x. One extra thing we need to 
consider only those pairs which have one element from ar1[] and other from ar2[], 
we use the boolean array for this purpose.

Can we do it in a single pass and O(1) extra space?
The idea is to start from left side of one array and 
right side of another array, and use the algorithm same as step 2 of above approach. 
Following is detailed algorithm.

1) Initialize a variable diff as infinite (Diff is used to store the
   difference between pair and x).  We need to find the minimum diff.
2) Initialize two index variables l and r in the given sorted array.
       (a) Initialize first to the leftmost index in ar1:  l = 0
       (b) Initialize second  the rightmost index in ar2:  r = n-1
3) Loop while l < m and r >= 0
       (a) If  abs(ar1[l] + ar2[r] - sum) < diff  then
           update diff and result
       (b) Else if(ar1[l] + ar2[r] <  sum )  then l++
       (c) Else r--
4) Print the result. 
'''
def printClosest(ar1, ar2, x):

    # import 
    import sys

    # Get the length
    m = len(ar1)
    n = len(ar2)

    # Initiaze the diff between pair sum and x
    diff = sys.maxint

    # Start from left side of ar1 and right side of ar2
    l = 0
    r = n-1
    while l < m and r >= 0:
        # If this pair is closer to x than the previously 
        # found closest, then update res_l, res_r and diff
        if abs(ar1[l] + ar2[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(ar1[l] + ar2[r] - x)

        # If sum of this pair is more than x, move to smaller side
        if ar1[l] + ar2[r] > x:
            r -= 1
        else:
            l += 1

    print ar1[res_l], ar2[res_r]

'''
7 30
1 30
7 40
'''
if __name__ == "__main__":
    ar1 = [1, 4, 5, 7]
    ar2 = [10, 20, 30, 40]
    x = 38
    printClosest(ar1, ar2, x)

    ar1 = [1, 4, 5, 7]
    ar2 = [10, 20, 30, 40]
    x = 32
    printClosest(ar1, ar2, x)

    ar1 = [1, 4, 5, 7]
    ar2 = [10, 20, 30, 40]
    x = 50
    printClosest(ar1, ar2, x)    
