'''
bubble sort

Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.
Sorting In Place: Yes
Stable: Yes
Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm.
In computer graphics it is popular for its capability to detect a very small error (like swap of just two elements)
in almost-sorted arrays and fix it with just linear complexity (2n). For example, it is used in a polygon filling 
algorithm, where bounding lines are sorted by their x coordinate at a specific scan line (a line parallel to x axis) 
and with incrementing y their order changes (two elements are swapped) only at intersections of two lines 
'''
def bubbleSort(theSeq):

    n = len(theSeq)
    for i in range(n-1):
        for j in range(n-i-1):
            if theSeq[j] > theSeq[j+1]:
                theSeq[j],theSeq[j+1] = theSeq[j+1],theSeq[j]

'''
Optimize bubble sort

if the sequence is sorted, it will use O(n),
otherwise, it will use O(n*n)
'''
def bubbleSortOptimize(theSeq):

    n = len(theSeq)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if theSeq[j] > theSeq[j+1]:
                swap = True
                theSeq[j],theSeq[j+1] = theSeq[j+1],theSeq[j]

        if swap is False:
            break

if __name__ == "__main__":
    theSeq = [-1, 0, -2, 4, 3, 7, 6]
    bubbleSort(theSeq)
    print theSeq
    theSeq = [-1, 0, -2, 4, 3, 7, 6]
    bubbleSortOptimize(theSeq)
    print theSeq

    theSeq = range(-10000,10000)
    bubbleSort(theSeq)
    print theSeq
    theSeq = range(-10000,10000)
    bubbleSortOptimize(theSeq)
    print theSeq
