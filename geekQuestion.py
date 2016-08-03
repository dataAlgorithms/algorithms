1. Reverse a string
def reverse_string(aString=None):

    if aString is None:
        return

    aString = [s for s in aString]

    n = len(aString)
    i = 0
    j = n-1
    while i < n/2:
        aString[i],aString[j]=aString[j],aString[i]
        i += 1
        j -= 1

    aString = ''.join(aString)

    print aString

2. reverse string without affecting special character
eg. 
Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"
def reverse_string_without_affect_special_character(aString=None):

    if aString is None:
        return

    aString = [s for s in aString]

    n = len(aString)
    i = 0
    j = n-1
    while i < j:
        if not aString[i].isalnum():
            i += 1
            continue
        if not aString[j].isalnum():
            j -= 1
            continue

        aString[i],aString[j]=aString[j],aString[i]
        i += 1
        j -= 1

    aString = ''.join(aString)

    print aString

3. Find longest palindromic sub string
def longestPalSubStr(aStr=None):

    '''
    longestPalSubStr("forgeekskeegfor")
    longestPalSubStr("forgeeksskeegfor")
    longestPalSubStr("123121212")
    longestPalSubStr("keeg")

    geekskeeg
    geeksskeeg
    12121
    ee
    '''

    if aStr is None:
        return

    n = len(aStr)
    maxLength = 1
    start = None

    for i in range(1, n):
        low = i-1
        high = i
        while low >= 0 and high < n and aStr[low] == aStr[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1

            low -= 1
            high += 1

        low = i-1
        high = i+1
        while low >= 0 and high < n and aStr[low] == aStr[high]:
            if high - low + 1 > maxLength:
                start = low
                maxLength = high - low + 1

            low -= 1
            high += 1

    if start is not None:
        print aStr[start:start+maxLength]
    else:
        print 'not found!'
        
4. Find triple whose sum is equal to specfic value
def findTripleSum(theSeq, theSum):

    theSeq = sorted(theSeq)
    n = len(theSeq)
    num = 0
    tmpList = []
    for i in range(0, n-2):
        j = i+1
        k = n - 1
        while j < k:
            if theSeq[i] + theSeq[j] + theSeq[k] >= theSum:
                k -= 1
            else:
                tmp = k
                while j < tmp:
                    tmpList.append([theSeq[i],theSeq[j],theSeq[tmp]])
                    tmp -= 1

                num += (k-j)
                j += 1
    print tmpList
    print num
    
5. Given an array of distinct elements, rearrange the elements of array in zig-zag fashion in O(n) time. 
The converted array should be in form a < b > c < d > e < f.
def zigZaq(theSeq):

    n = len(theSeq)
    flag = True
    for i in range(0, n-1):
        if flag:
            if theSeq[i] > theSeq[i+1]:
                theSeq[i],theSeq[i+1] = theSeq[i+1],theSeq[i]
        else:
            if theSeq[i] < theSeq[i+1]:
                theSeq[i],theSeq[i+1] = theSeq[i+1],theSeq[i]

        flag = not flag

6. Generate all possible sorted arrays from alternate elements of two given sorted arrays
# Driver program
def alternateItems():

    # Wrapper function
    def generate(aList, bList, m, n):

        cList = [0 for _ in range(m+n)]
        generateUtil(aList, bList, cList, 0, 0, m, n, 0, True)

    '''
    /* Function to generates and prints all sorted arrays from alternate elements of
       'A[i..m-1]' and 'B[j..n-1]'
       If 'flag' is true, then current element is to be included from A otherwise
       from B.
       'len' is the index in output array C[]. We print output  array  each time
       before including a character from A only if length of output array is
       greater than 0. We try than all possible combinations */
    '''
    def generateUtil(aList, bList, cList, i, j, m, n, l, flag):
    
        if flag:
            if l:
                printArr(cList, l+1)
    
            for k in range(i, m):
                if not l:
                    cList[l] = aList[k]
                    generateUtil(aList, bList, cList, k+1, j, m, n, l, not flag)
                else:
                    if aList[k] > cList[l]:
                        cList[l+1] = aList[k]
                        generateUtil(aList, bList, cList, k+1, j, m, n, l+1, not flag)
        else:
            for p in range(j, n):
                if bList[p] > cList[l]:
                    cList[l+1] = bList[p]
                    generateUtil(aList, bList, cList, i, p+1, m, n, l+1, not flag)
    
    # A utility function to print an array
    def printArr(arr, n):
        for i in range(n):
            print arr[i],
        print ''
            
    aList = [10, 15, 25]
    bList = [5, 20, 30]
    n = len(aList)
    m = len(bList)
    generate(aList, bList, n, m)
       
"""
Output:
10 20 
10 20 25 30 
10 30 
15 20 
15 20 25 30 
15 30 
25 30 
"""
if __name__ == "__main__":
    alternateItems()

#7. Pythagorean triplet
def isTriplet(aList=[3, 1, 4, 6, 5]):

    n = len(aList)
    for i in range(n):
        aList[i] = aList[i] * aList[i]

    sorted(aList)

    for i in range(n-1, 1, -1):
        l = 0
        r = i - 1
        while l < r:
            if aList[l] + aList[r] == aList[i]:
                return True
        
            if aList[l] + aList[r] < aList[i]:
                l += 1
            else:
                r -= 1

    return False

"""
Output
True
False
"""
if __name__ == "__main__":
    print isTriplet()   #True
    print isTriplet(aList=[10, 4, 6, 12, 5]) #False

#8. Given a sorted array (sorted in non-decreasing order) of positive numbers, 
# find the smallest positive integer value that cannot be represented as sum of elements of any subset of given set. 
def findSmallNotSum(aList):

    res = 1
    i = 0
    n = len(aList)
    while i < n and aList[i] <= res:
        res += aList[i]
        i += 1

    return res

"""
2
5
10
4
22
"""
if __name__ == "__main__":

    for aList in [[1, 3, 6, 10, 11, 15], [1, 1, 1, 1],
                 [1, 1, 3, 4], [1, 2, 5, 10, 20, 40],
                 [1, 2, 3, 4, 5, 6]]:
        print findSmallNotSum(aList)   

#9. Given an array of integers and a number x, 
# find the smallest subarray with sum greater than the given value.
def smallestSubWithSum(aList, x):

    curr_sum = 0
    n = len(aList)
    min_len = n + 1

    bList = []
    start = 0
    end = 0
    while end < n:
        while curr_sum <= x and end < n:
            curr_sum += aList[end]
            end += 1

        while curr_sum > x and start < n:
            if end - start < min_len:
                min_len = end - start
                bList = aList[start:end]
            
            curr_sum -= aList[start]
            start += 1

    return min_len, bList

"""
(3, [4, 45, 6])
(1, [10])
(4, [100, 1, 0, 200])
"""
if __name__ == "__main__":
    aList = [1, 4, 45, 6, 0, 19]
    x = 51
    print smallestSubWithSum(aList, x)

    aList = [1, 10, 5, 2, 7]
    x = 9
    print smallestSubWithSum(aList, x)

    aList = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
    x = 280
    print smallestSubWithSum(aList, x)

# 10 Stock Buy Sell to Maximize Profit
# The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days. 
def stockBuySell(price):

    class Interval:
        # Init
        def __init__(self):
            self.buy = None
            self.sell = None
        
    n = len(price)
    if n == 1:
        return

    count = 0
    interval = Interval
    sol = [interval() for i in range(n/2+1)]

    i = 0
    while i < n-1:
        while i < n-1 and price[i+1] <= price[i]:
            i += 1

        if i == n-1:
            break

        sol[count].buy = i
        i += 1

        while i < n and price[i] >= price[i-1]:
            i += 1

        sol[count].sell = i-1

        count += 1


    if count == 0:
        print 'no day!'
    else:
        for i in range(count):
            print 'buy on day:%d\t sell on day:%d\n' % (sol[i].buy, sol[i].sell)

"""
buy on day:0     sell on day:3
buy on day:4     sell on day:6
"""
if __name__ == "__main__":
    price = [100, 180, 260, 310, 40, 535, 695]
    stockBuySell(price)        

11. Find the maximum subarray XOR in a given array
Given an array of integers. 

def maxSubarrayXOR(arr):


    n = len(arr)
    aList = [[] for i in range(n)]

    sumList = []
    for i in range(0, n):

        curr_xor = 0
        bList = []
        ans = 0
        for j in range(i, n):

            curr_xor = curr_xor ^ arr[j]        
            if curr_xor > ans:
                ans = curr_xor
                bList.append(arr[j])
            else:
                break

        aList[i] = bList
        sumList.append(ans)

    theIndex = 0
    theSum = sumList[0]
    for i in range(len(sumList)):
        if sumList[i] > theSum:
            theIndex = i
            theSum = sumList[i]

    maxList = aList[theIndex]

    print 'maxList:', maxList
    print 'maxSum:', theSum
    return theSum,maxList

def max_xor_opt(iterable):
    array = list(iterable)  # make it a list so that we can iterate it twice
    if not array:  # special case the empty array to avoid an empty max
        return 0
    x = 0
    while True:
        y = max(array)
        print 'y:', y
        if y == 0:
            return x
        # y has the leading 1 in the array
        x = max(x, x ^ y)
        # eliminate
        array = [min(z, z ^ y) for z in array]

"""
maxList: [1, 2, 12]
maxSum: 15
(15, [1, 2, 12])
"""
if __name__ == "__main__":
    iterable = [8, 1, 2, 12, 7, 6]
    print maxSubarrayXOR(iterable)

12. A magic number is defined as a number which can be expressed as a power of 5 or sum of unique powers of 5. 
First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….

Write a function to find the n’th Magic number.

Example:

Input: n = 2
Output: 25

Input: n = 5
Output: 130 


If we notice carefully the magic numbers can be represented as 001, 010, 011, 100, 101, 110 etc,
 where 001 is 0*pow(5,3) + 0*pow(5,2) + 1*pow(5,1).
       010 is 0*pow(5,3) + 1*pow(5,2) + 0*pow(5,1)
       011 is 0*pow(5,3) + 1*pow(5,2) + 1*pow(5,1)
       

def nthMagicNo(n):

    pow = 1
    answer = 0

    while n:
        pow = pow * 5

        # If lastbit of n is set
        if n & 1:
            answer += pow

        # proceed to next bit
        n /= 2

    print answer
    return answer

"""
5
25
30
125
130
"""
if __name__ == "__main__":
    for i in range(1, 6):
        nthMagicNo(i)

13. Given an integer array of n integers, find sum of 
bit differences in all pairs that can be formed from array elements.

 Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y. 
For example, bit difference for 2 and 7 is 2. 
Binary representation of 2 is 010 and 7 is 111 
( first and last bits differ in two numbers).

Examples:

Input: arr[] = {1, 2}
Output: 4
All pairs in array are (1, 1), (1, 2)
                       (2, 1), (2, 2)
Sum of bit differences = 0 + 2 +
                         2 + 0
                      = 4

def sumBitDiff(arr):

    ans = 0
    n = len(arr)
    
    # traverse over all bits
    for i in range(0, 32):
        count = 0
        for j in range(0, n):
            if arr[j] & (1 << i):
                count += 1

        # add count * (n-count)*2 to the answer
        ans += (count * (n - count) * 2)

    return ans

"""
4
26
"""
if __name__ == "__main__":
    arr = [1, 2]
    print sumBitDiff(arr)

    arr = [1, 3, 7, 8]
    print sumBitDiff(arr)

14. Find the element that appears once
Given an array where every element occurs three times, except one element
which occurs only once. Find the element that occurs once. 
Expected time complexity is O(n) and O(1) extra space.
Examples:

Input: arr[] = {12, 1, 12, 3, 12, 1, 1, 2, 3, 3}
Output: 2

def getSingle(arr):

    '''
    Following is another O(n) time complexity and O(1) extra space method suggested by aj. 
    We can sum the bits in same positions for all the numbers and take modulo with 3. 
    The bits for which sum is not multiple of 3, are the bits of number with single occurrence.  
    Let us consider the example array {5, 5, 5, 8}. The 101, 101, 101, 1000
    Sum of first bits%3 = (1 + 1 + 1 + 0)%3 = 0;
    Sum of second bits%3 = (0 + 0 + 0 + 0)%0 = 0;
    Sum of third bits%3 = (1 + 1 + 1 + 0)%3 = 0;
    Sum of fourth bits%3 = (1)%3 = 1;
    Hence number which appears once is 1000
    '''
    INT_SIZE = 32
    result = 0
    n = len(arr)

    # Iterate through every bit
    for i in range(0, INT_SIZE):
        # Find sum of set bits at ith position in all
        # array elements
        theSum = 0
        x = (1 << i)
        for j in range(0, n):
            if arr[j] & x:
                theSum += 1

        # The bits with sum not multiple of 3,
        # are the bits of element with single occurrence
        if theSum %3:
            result |= x

    return result

if __name__ == "__main__":
    arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7]
    print getSingle(arr)
    arr = [12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
    print getSingle(arr)

15. convert number to any radix
def numToAny(n, base=2):

    if n > 1:
        numToAny(n/base, base=base)

    if base != 16:
        print n%base,
    else:
        baseDict = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        if n%base in [10,11,12,13,14,15]:
            print baseDict[n%base],
        else:
            print n%base,

'''
1 1 1
1 0 0
1 1 0 0
0 9 6
0 2 2 5
'''
if __name__ == "__main__":
    for n in [7, 4, 12]:
        numToAny(n)
        print ''

    numToAny(150, 16)
    print ''

    numToAny(149, 8)
