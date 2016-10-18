#! coding=utf-8

import math 

def insertSort(theSeq):

    n = len(theSeq)
    for i in range(1,n):
        pos = i
        pivot = theSeq[pos]
        while pos > 0 and pivot < theSeq[pos-1]:
            theSeq[pos] = theSeq[pos-1]
            pos = pos - 1

        theSeq[pos] = pivot
        
def bucketSort(array, bucketSize=2):
    if len(array) == 0:
        return array

    # Determine minimum and maximum values
    minValue = array[0]
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] < minValue:
            minValue = array[i]
        elif array[i] > maxValue:
            maxValue = array[i]

    # Initialize buckets
    bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
    bucketCount = int(bucketCount)
    
    print 'bucketCount:', bucketCount
    buckets = []
    for i in range(0, bucketCount):
        buckets.append([])

    # Distribute input array values into buckets
    for i in range(0, len(array)):
        buckets[int(math.floor((array[i] - minValue) / bucketSize))].append(array[i])

    print 'buckets:', buckets
    
    # Sort buckets and place back into input array
    array = []
    for i in range(0, len(buckets)):
        insertSort(buckets[i])
        for j in range(0, len(buckets[i])):
            array.append(buckets[i][j])

    return array

'''
aList = [9, 10, 7 ,3, 87, 9, 119]
bucketCount: 59
buckets: [[3], [], [7], [9, 10, 9], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [87], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [119]]
[3, 7, 9, 9, 10, 87, 119]

aList = [0.0, 0.2, 0.1, 0.5, 0.3, 0.4]
bucketCount: 1
buckets: [[0.0, 0.2, 0.1, 0.5, 0.3, 0.4]]
[0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
'''
if __name__ == "__main__":
    aList = [9, 10, 7 ,3, 87, 9, 119]
    newList = bucketSort(aList)
    print newList
