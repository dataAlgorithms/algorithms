#! coding-utf8 

'''
1. radix sort


The lower bound for Comparison based sorting algorithm
(Merge Sort, Heap Sort, Quick-Sort .. etc) is Ω(nLogn), i.e., they cannot do better than nLogn.

Counting sort is a linear time sorting algorithm that sort in O(n+k) time
when elements are in range from 1 to k.

What if the elements are in range from 1 to n2?
We can’t use counting sort because counting sort will take O(n2) which is worse
than comparison based sorting algorithms. Can we sort such an array in linear time?
Radix Sort is the answer. The idea of Radix Sort is to do digit by digit sort starting
from least significant digit to most significant digit. Radix sort uses counting sort as a subroutine to sort.

The Radix Sort Algorithm
1) Do following for each digit i where i varies from least significant digit to the most significant digit.
………….a) Sort input array using counting sort (or any stable sort) according to the i’th digit.

Example:
Original, unsorted list:

170, 45, 75, 90, 802, 24, 2, 66
Sorting by least significant digit (1s place) gives: [*Notice that we keep 802 before 2, because 802 occurred
before 2 in the original list, and similarly for pairs 170 & 90 and 45 & 75.]

170, 90, 802, 2, 24, 45, 75, 66
Sorting by next digit (10s place) gives: [*Notice that 802 again comes before 2 as 802 comes before 2 in the previous list.]

802, 2, 24, 45, 66, 170, 75, 90
Sorting by most significant digit (100s place) gives:

2, 24, 45, 66, 75, 90, 170, 802

What is the running time of Radix Sort?
Let there be d digits in input integers. Radix Sort takes O(d*(n+b)) time where b is the base for representing numbers,
for example, for decimal system, b is 10. What is the value of d? If k is the maximum possible value, then d would be O(logb(k)).
So overall time complexity is O((n+b) * logb(k)). Which looks more than the time complexity of comparison based sorting algorithms 
for a large k.

Let us first limit k. Let k <= nc where c is a constant. In that case, the complexity becomes O(nLogb(n)).
But it still doesn’t beat comparison based sorting algorithms.
What if we make value of b larger?. What should be the value of b to make the time complexity linear?
If we set b as n, we get the time complexity as O(n). In other words, we can sort an array of integers
with range from 1 to nc if the numbers are represented in base n (or every digit takes log2(n) bits).

Is Radix Sort preferable to Comparison based sorting algorithms like Quick-Sort?
If we have log2n bits for every digit, the running time of Radix appears to be better than Quick Sort for a wide range of input 
numbers.
The constant factors hidden in asymptotic notation are higher for Radix Sort and Quick-Sort uses hardware caches more effectively.
Also, Radix sort uses counting sort as a subroutine and counting sort takes extra space to sort numbers.
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

'''
3. Radix sort (support negative value)
'''
from math import log
 
def getDigit(num, base, digit_num):
    # pulls the selected digit
    return (num // base ** digit_num) % base  
 
def makeBlanks(size):
    # create a list of empty lists to hold the split by digit
    return [ [] for i in range(size) ]  
 
def split(a_list, base, digit_num):
    buckets = makeBlanks(base)
    for num in a_list:
        # append the number to the list selected by the digit
        buckets[getDigit(num, base, digit_num)].append(num)  
    return buckets
 
# concatenate the lists back in order for the next step
def merge(a_list):
    new_list = []
    for sublist in a_list:
       new_list.extend(sublist)
    return new_list
 
def maxAbs(a_list):
    # largest abs value element of a list
    return max(abs(num) for num in a_list)
 
def split_by_sign(a_list):
    # splits values by sign - negative values go to the first bucket,
    # non-negative ones into the second
    buckets = [[], []]
    for num in a_list:
        if num < 0:
            buckets[0].append(num)
        else:
            buckets[1].append(num)
    return buckets
 
def radixSort(a_list, base):
    # there are as many passes as there are digits in the longest number
    passes = int(round(log(maxAbs(a_list), base)) + 1) 
    new_list = list(a_list)
    for digit_num in range(passes):
        new_list = merge(split(new_list, base, digit_num))
    return merge(split_by_sign(new_list))
