'''
Problem Statement: Given an array of N distinct integers, find floor value of input ‘key’
Say, A = {-1, 2, 3, 5, 6, 8, 9, 10} and key = 7, we should return 6 as outcome.

We can use the above optimized implementation to find floor value of key.
We keep moving the left pointer to right most as long as the invariant holds. Eventually left 
pointer points an element less than or equal to key (by definition floor value). The following are possible corner cases,

—> If all elements in the array are smaller than key, left pointer moves till last element.
—> If all elements in the array are greater than key, it is an error condition.
—> If all elements in the array equal and <= key, it is worst case input to our implementation.
'''
def floor(aList, key):
    
    def toFloor(aList, l, r, key):
    
        while r-l > 1:
            m = (l+r) // 2
            if aList[m] <= key:
                l = m
            else:
                r = m
    
        return aList[l]

    # add error check if key < aList[0]
    if key < aList[0]:
        return -1

    return toFloor(aList, 0, len(aList)-1, key)

'''
6
'''
if __name__ == "__main__":
    aList = [-1, 2, 3, 5, 6, 8, 9, 10]
    key = 7
    print floor(aList, key)
