#! coding-utf8 

'''
1. radix sort
'''
def radixSort(a, radix=10, debug=0):

    def getMaxDigitNum(a, radix=10, debug=1):
        intList = [int(item) for item in a]
        maxItem = max(intList)

        count = 0
        j = 1
        while maxItem  >= 1:
            maxItem  /= j
            count += 1
            j *= radix

        if debug == 1:
            print count

        return count

    k = getMaxDigitNum(a, radix=10, debug=0)
    buckets = [[] for i in range(radix)]
    for i in range(1, k+1):
        for key in a:
            buckets[key%(radix**i)/(radix**(i-1))].append(key)

        del a[:]
        for each in buckets:
            a.extend(each)

        buckets = [[] for i in range(radix)]

    if debug == 1:
        print a

    return a

'''
theSeq sorted after: [5, 5, 10, 10, 13, 13, 18, 18, 23, 23, 29, 29, 31, 31, 37, 37, 40, 49, 51, 51, 54, 54, 62, 62, 87, 89]
'''
if __name__ == "__main__":
    theSeq = [23,23,10,10,18,18,51,51,5,5,13,13,31,31,54,54,49,40,62,62,29,29,89,87,37,37]
    newSeq = radixSort(theSeq)
    print 'theSeq sorted after:', newSeq 
