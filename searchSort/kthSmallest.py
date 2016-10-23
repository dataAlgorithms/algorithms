'''
Method 1 (Simple Solution) 
A Simple Solution is to sort the given array using a O(nlogn) sorting algorithm like Merge Sort, Heap Sort, etc and return the element at index k-1 in the sorted array. Time Complexity of this solution is O(nLogn).
'''
def kthSmallest(theSeq, k):

    # Sort the sequence
    theSeq = sorted(theSeq)

    # Print the kth element
    print theSeq[k-1]

'''
7
3
'''
if __name__ == "__main__":

    for theSeq in [[12, 3, 5, 7, 19], [1,2,3,4,5]]:
        kthSmallest(theSeq, 3)

# This function returns kth smallest element in distinct arr[l..r]
# using quickSort based method,
# Assumption: elements in arr[] are distinct
def kthSmallest(arr, l, r, k):

    import random

    # standard partion process of quickSort
    # it considers the last element as pivot
    # and moves all smaller element to left of it and
    # greater elements to right, 
    # the function is used by randomPartition()
    def partition(arr, l, r):
        x = arr[r]
        i = l

        for j in range(l, r):
            if arr[j] <= x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i],arr[r] = arr[r], arr[i]
        return i

    # Picks a random pivot element between l and r and partitions
    # arr[l..r] arount the randomly picked element using partition
    def randomPartition(arr, l, r):
        n = r - l + 1
        pivot = random.randrange(n)
        arr[l+pivot],arr[r] = arr[r],arr[l+pivot]
        return partition(arr, l, r) 

    # If k is smaller than number of elements in array
    if k > 0 and k <= r - l + 1:
        # Partion the array around a random element and
        # get position of pivot element in sorted array
        pos = randomPartition(arr, l, r)

        # If position is the same as k
        if pos-l == k-1:
            return arr[pos]

        # If position is more, recur for left subarray
        if pos-l > k-1:
            return kthSmallest(arr, l, pos-1, k)

        # Else recur for right subarray
        return kthSmallest(arr, pos+1, r, k-pos+l-1)

    return -1

'''
7
10
5
'''
if __name__ == "__main__":
    for arr,k in [[[7, 10, 4, 3, 20, 15], 3], [[7, 10, 4, 3, 20, 15], 4], [[12, 3, 5, 7, 4, 19, 26], 3]]:
        print kthSmallest(arr, 0, len(arr)-1, k)
