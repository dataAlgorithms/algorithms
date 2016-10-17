'''
Comb Sort is mainly an improvement over Bubble Sort. 
Bubble sort always compares adjacent values. 
So all inversions are removed one by one. 
Comb Sort improves on Bubble Sort by using gap of size more than 1. 
The gap starts with a large value and shrinks by a factor of 1.3 
in every iteration until it reaches the value 1. 
Thus Comb Sort removes more than one inversion counts with one swap 
and performs better than Bublle Sort.

The shrink factor has been empirically found to be 1.3 
(by testing Combsort on over 200,000 random lists) [Source: Wiki]

Although, it works better than Bubble Sort on average, worst case remains O(n2).
'''
# find gap between elements
def getNextGap(gap=None):

    # shrink gap by shrink factor
    gap = (gap * 10) / 13

    if gap < 1:
        return 1

    return gap

# sort a a[0..n-1] using comb sort
def combSort(theSeq):

    # get the length
    n = len(theSeq)

    # Initialize gap
    gap = n

    # Initialize swapped as true to make sure that loop runs
    swapped = True

    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap != 1 or swapped is True:
        # Find next gap
        gap = getNextGap(gap)

        # Initialize swapped as false so that we can 
        # check if swap happened or not
        swapped = False

        # Compare all elements with current gap
        for i in range(0, n-gap):
            if theSeq[i] > theSeq[i+gap]:
                theSeq[i],theSeq[i+gap] = theSeq[i+gap],theSeq[i]
                swapped = True

if __name__ == "__main__":
    theSeq = [6, 4, 1, 56, 3, -44, 23, -6, 28, 0]
    combSort(theSeq)
    print theSeq
