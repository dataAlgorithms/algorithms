'''
A recursive ternary search function. It returns location of x in
given array arr[l..r] is present, otherwise -1
'''
def ternarySearch(arr, l, r, x):

    if r >= l:
        mid1 = l + (r-l)//3
        mid2 = mid1 + (r-l)//3

        # If x is present at the mid1
        if arr[mid1] == x:
            return mid1

        # If x is present at the mid2
        if arr[mid2] == x:
            return mid2

        # If x is present in left one-third
        if arr[mid1] > x:
            return ternarySearch(arr, l, mid1-1, x)

        # If x is present in right one-third
        if arr[mid2] < x:
            return ternarySearch(arr, mid2+1, r, x)

        # If x is present in middle one-third
        return ternarySearch(arr, mid1+1, mid2-1, x)

    return -1

'''
3
'''
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6, 9, 10]
    l = 0
    r = len(arr)-1
    x = 4
    print ternarySearch(arr, l, r, x)
