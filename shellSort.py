#! coding=utf-8

def shellSort(aList):

    sublistCount = len(aList) // 2
    while sublistCount > 0:
 
        for startposition in range(sublistCount):
            gapInsertionSort(aList, startposition, sublistCount)

        print 'After increment of size %s, the list is %s' % (sublistCount, aList)

        sublistCount = sublistCount // 2

def gapInsertionSort(aList, start, gap):

    for i in range(start+gap, len(aList), gap):

        currentvalue = aList[i]
        position = i

        while position >= gap and aList[position-gap] > currentvalue:
            aList[position] = aList[position-gap]
            position = position - gap

        aList[position] = currentvalue

'''
aList sorted before: [42, 8, 15, 60, 25, 96, 35, 82, 3, 63]
After increment of size 5, the list is [42, 8, 15, 3, 25, 96, 35, 82, 60, 63]
After increment of size 2, the list is [15, 3, 25, 8, 35, 63, 42, 82, 60, 96]
After increment of size 1, the list is [3, 8, 15, 25, 35, 42, 60, 63, 82, 96]
aList sorted after: [3, 8, 15, 25, 35, 42, 60, 63, 82, 96]
'''
if __name__ == "__main__":
    import random
    aList = [random.randrange(100) % 100 for _ in range(10)]
    print 'aList sorted before:', aList
    shellSort(aList)
    print 'aList sorted after:', aList
