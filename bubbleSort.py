'''
bubble sort

O(n*n)
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
