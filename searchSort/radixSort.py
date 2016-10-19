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

'''
2. new radix sort
'''
# A function to do counting sort of arr according to 
# the digit represented by exp
def countingSort(arr, exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * n

    # initialize count array as 0
    count = [0] * 10

    # Store count of occurrences in count
    for i in range(0, n):
        index = (arr[i]/exp1)
        count[(index)%10] += 1

    # Change count[i] so that count[i] now contais actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i-1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i]/exp1)
        output[count[(index)%10]-1] = arr[i]
        count[(index)%10] -= 1
        i -= 1

    # Copying the output array to arr
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

# Method to do Radix sort
def radixSort(arr):

    # Find the maximum number fo know number of digits
    max1 = max(arr)

    # Do counting sort for every digit, Note that instead
    # of passing digit number, exp is passed, exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 /exp > 0:
        countingSort(arr, exp)
        exp *= 10

'''
2 24 45 66 75 90 170 802
'''
if __name__ == "__main__":
    arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
    radixSort(arr)

    for i in range(len(arr)):
        print(arr[i]),
