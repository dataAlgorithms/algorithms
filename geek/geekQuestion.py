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
        
4. Find triple whose sum is less than specfic value
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

16. Returns count of set bits present in all numbers from 1 to n
'''
Return position of leftmost set bit
The rightmost position is considered as 0
'''
def getLeftmostBit(n):

    m = 0
    while n > 1:
        n = n >> 1
        m += 1

    return m

'''
Given the position of previous leftmost set bit in n (
or an upper bound on leftmost position) returns the new
position of leftmost set bit in n
'''
def getNextLeftmostBit(n, m):
    temp = 1 << m
    while n < temp:
        temp = temp >> 1
        m -= 1

    return m

'''
Returns count of set bits present in all numbers from 1 to n
'''
def countSetBits(n):

    # Get the position of leftmost set bit in n, this will be
    # used as an upper bound for next set bit function
    m = getLeftmostBit(n)

    # Use the position
    return _countSetBits(n, m)

'''
recursive function used by ocuntSetBits
'''
def _countSetBits(n, m):

    # Base case: if n is 0, then set bit count is 0
    if n == 0:
        return 0

    # get position of next leftmost set bit
    m = getNextLeftmostBit(n, m)

    # if n is of the form 2^x-1, if n is like 1, 3, 7, 15, 31...etc
    # then we are done
    # since positions are considered starting from 0, 1 is added to m
    if n == (1<<(m+1)) -1:
        return (m+1)*(1<<m)

    # update n for next recursive call
    n = n - (1<<m)
    return (n+1) + countSetBits(n) + m*(1<<(m-1))

'''
4
9
12
13
35
'''
if __name__ == "__main__":
    for n in [3, 6, 7, 8, 17]:
        print countSetBits(n)

17. Rotate bits of a number
Bit Rotation: A rotation (or circular shift) is an operation similar to shift except that
 the bits that fall off at one end are put back to the other end.
def rotateBit(n, d, flag=0):

    '''
    n, primary number
    d, rotate bit number
    flag=0, left rotate
    flag=1, right rotate
    '''

    INT_BITS = 32

    def leftRotate(n, d):
        '''
        In n<<d, last d bits are 0, To put first 3 bits of n at
        last, do bitwise or of n<<d with n >> (INT_BITS - d)
        '''
        return (n << d) or (n >> (INT_BITS - d))

    def rightRotate(n, d):
        '''
        In n>>d, first d tis are 0, To put last 3 bits of at
        first, do bitwise or of n>>d with n << (INT_BITS-d)
        '''
        return (n >> d) or (n << (INT_BITS -d))

    if flag == 0:
        return leftRotate(n, d)
    else:
        return rightRotate(n, d)

"""
64
4
"""
if __name__ == "__main__":
    d  = 2
    n = 16
    print rotateBit(16, 2, 0)
    print rotateBit(16, 2, 1)

18. Count number of bits to be flipped to convert A to B
"""
Count number of bits to be flipped to convert A to B

eg.
   A  = 1001001  73
   B  = 0010101  21
   a_xor_b = 1011100
   No of bits need to flipped = set bit count in a_xor_b i.e. 4
"""
def countBit(a, b):

    count = 0
    c = a^b
    while c != 0:
        c &= (c-1)
        count += 1

    return count

"""
4
"""
if __name__ == "__main__":
    a = 73
    b = 21
    print countBit(a, b)
    
19. Given a number x, find the smallest Sparse number which greater than or equal to x
def nextSparse(x):

    '''
    Find binary representation of x and store it in binList
    binList[0] contains least significant bit (LSB), next
    bin is in binList[1], and so on
    '''

    binList = []
    while x != 0:
        binList.append(x&1)
        x >>= 1

    # There are be extra bit in result, so add one extra bit
    binList.append(0)

    # Get the size of binary representation
    n = len(binList) 

    # The position till which all bits are finalized
    last_final = 0

    # Start from second bit (next to LSB)
    for i in range(1, n-1):
        # If current bit and its previous bit are 1, but next
        # bit is not 1
        if binList[i] == 1 and binList[i-1] == 1 and binList[i+1] != 1:
            # Make the next bit 1
            binList[i+1] = 1

            # Make all bits before current bit as 0 to make
            # sure that we get the smallest next number
            for j in range(i, last_final-1, -1):
                binList[j] = 0

            # Store position of the bit set so that this bit
            # and bits before it are not changed next time
            last_final = i+1

    # Find decimal equivalent of modified binList[]
    ans = 0
    for i in range(0, n):
        ans += binList[i]*(1<<i)

    return ans

'''
9
4
40
64
'''
if __name__ == "__main__":
    for i in [9, 4, 38, 44]:
        print nextSparse(i)

20. Modular Exponentiation (Power in Modular Arithmetic)
Given three numbers x, y and p, compute (xy) % p.
def power(x, y, p):

    # Initialize result
    res = 1

    # Update x if it is more than or equal to p
    x = x % p

    while y > 0:
        # If y is odd, multiply x with result
        if y & 1:
            res = (res*x) % p

        # y must be even now
        y = y>>1
        x = (x*x) % p

    return res

if __name__ == "__main__":
    x = 2
    y = 5
    p = 13
    print power(2, 5, 13)
    print (x**y)%p

21. Modular multiplicative inverse
Given two integers ‘a’ and ‘m’, find modular multiplicative inverse of ‘a’ under modulo ‘m’.

The modular multiplicative inverse is an integer ‘x’ such that.

 a x ≡ 1 (mod m) 
The value of x should be in {0, 1, 2, … m-1}, i.e., in the ring of integer modulo m.

The multiplicative inverse of “a modulo m” exists if and only if a and m are relatively prime (i.e., if gcd(a, m) = 1).

Examples:

Input:  a = 3, m = 11
Output: 4
Since (4*3) mod 11 = 1, 4 is modulo inverse of 3
One might think, 15 also as a valid output as "(15*3) mod 11" 
is also 1, but 15 is not in ring {0, 1, 2, ... 10}, so not 
valid.

Input:  a = 10, m = 17
Output: 12
Since (10*12) mod 17 = 1, 12 is modulo inverse of 3

def nvModInverse(a, m):

    a = a%m
    for x in range(1, m):
        if ((a*x) % m == 1):
            return x

def exModInverse(a, m):

    '''
    Works when m and a are coprime
    '''
    m0 = m
    x0 = 0
    x1 = 1

    if m == 1:
        return 0

    while a > 1:
        # q is quotient
        q = a / m
        t = m

        # m is remainder now, 
        m = a % m
        a = t

        t = x0
        x0 = x1 - q * x0
        x1 = t

    # make x1 positive
    if x1 < 0:
        x1 += m0

    return x1
 
def feModInverse(a, m):

    def gcd(a, b):
        if a == 0:
            return b

        return gcd(b%a, a)

    def power(x, y, m):
        if y == 0:
            return 1

        p = power(x, y/2, m) % m
        p = (p * p) % m

        if y%2 == 0:
            return p
        else:
            return (x * p) % m

    g = gcd(a, m)
    if g != 1:
        print 'Inverse does not exit!'
    else:
        # if a and m are relatively prime, then modulo inverse
        # is a^(m-2) mode m
        return power(a, m-2, m)

"""
4
4
4
"""
if __name__ == "__main__":
    a = 3
    m = 11
    print modInverse(a, m)
    print exModInverse(a, m)
    print feModInverse(a, m)

21. Check prime number
def isPrime(num):

    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print '%s is not a prime number!' % num
                break

        else:
            print '%s is a prime number!' % num

    else:
        print '%s is not a prime number!' % num

'''
1 is not a prime number!
2 is a prime number!
3 is a prime number!
4 is not a prime number!
5 is a prime number!
6 is not a prime number!
7 is a prime number!
8 is not a prime number!
'''
if __name__ == "__main__":
    for i in [1,2,3,4,5,6,7,8]:
        isPrime(i)

22. Calculate Eulere's Totient Function
'''
Euler’s Totient function Φ(n) for an input n is count of numbers 
in {1, 2, 3, …, n} that are relatively prime to n, i.e., 
the numbers whose GCD (Greatest Common Divisor) with n is 1.

Examples:

Φ(1) = 1  
gcd(1, 1) is 1

Φ(2) = 1
gcd(1, 2) is 1, but gcd(2, 2) is 2.

Φ(3) = 2
gcd(1, 3) is 1 and gcd(2, 3) is 1

Φ(4) = 2
gcd(1, 4) is 1 and gcd(3, 4) is 1

Φ(5) = 4
gcd(1, 5) is 1, gcd(2, 5) is 1, 
gcd(3, 5) is 1 and gcd(4, 5) is 1

Φ(6) = 2
gcd(1, 6) is 1 and gcd(5, 6) is 1, 
How to compute Φ(n) for an input n?
'''

def phi(n):

    # Initialize result as n
    result = n

    # Consider all prime factors of n and subtract their
    # multiples from result
    p = 2
    while p*p <= n:
        # Check if p is a prime factor
        if n % p == 0:
            # If yes, then update n and result
            while n % p == 0:
                n /= p
            result -= result/p

        p += 1

    # If n has a prime factor greater than sqrt
    # there can be at most one such prime factor
    if n > 1:
        result -= result / n

    return result

'''
phi(1): 1
phi(2): 1
phi(3): 2
phi(4): 2
phi(5): 4
phi(6): 2
phi(7): 6
phi(8): 4
phi(9): 6
phi(10): 4
'''
if __name__ == "__main__":
    for n in range(1, 11):
        print 'phi(%s): %s' % (n,phi(n))

23. Sieve of Eratosthenes,
Given a number n, print all primes smaller than or equal to n.

def SieveofEratosthenes(n):

    # Create a boolean array prime[0..n] and initialize
    # all entries it as true, A value in prime[i] will
    # finally be false if i is not a prime, else true
    prime = [True] * (n+1)

    p = 2
    while p*p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # update all multiples of p
            i = p*2
            while i <= n:
                prime[i] = False
                i += p

        p += 1

    # Print all prime number
    for p in range(2, n+1):
        if prime[p]:
            print p,

'''
2 3 5 7 11 13 17 19 23 29
'''
if __name__ == "__main__":
    n = 30
    SieveofEratosthenes(n)
    
24. Convex Hull
class Point:
    # Init
    def __init__(self, x, y):
        self.x = x
        self.y = y


'''
Find orientation of ordered triplet (p, q, r)
the function returns following values
0 ..>p, q and r are colinear
1 ..>clockwise
2 ..>counterclockwise
'''
def orientation(p, q, r):

    val = (q.y - p.y) * (r.x - q.x) - \
            (q.x - p.x) * (r.y - q.y)

    # colinear
    if val == 0:
        return 0

    # clock or counterclock wise
    if val > 0:
        return 1
    else:
        return 2

# Prints convex hull of a set of n points
def convexHull(points, n):

    # There must be at least 3 points
    if n < 3:
        return


    # Initialize result
    hull = []

    # Find the leftmost point
    l = 0
    for i in range(l, n):
        if points[i].x < points[l].x:
            l = i
    
    '''
    Start from leftmost point, keep moving counterclockwise
    until reach the start point again.  This loop runs O(h)
    times where h is number of points in result or output.
    '''
    p = l

    while True:

        # add current point to result
        hull.append(points[p])

        '''
        Search for a point 'q' such that orientation(p, x,
        q) is counterclockwise for all points 'x'. The idea
        is to keep track of last visited most counterclock-
        wise point in q. If any point 'i' is more counterclock-
        wise than q, then update q.
        '''
        q = (p+1)%n
        for i in range(0, n):
            # If i is more counterclockwise than current q, then update q
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        
        '''
        Now q is the most counterclockwise with respect to p
        Set p as q for next iteration, so that q is added to
        result 'hull'
        '''
        p = q

        if p == l:
            break

    # Print result
    for i in range(0, len(hull)):
        print "(" + str(hull[i].x) + "," + str(hull[i].y) + ")"

'''
(0,3)
(0,0)
(3,0)
(3,3)

'''
if __name__ == "__main__":
    #points = [[0, 3], [2, 2], [1, 1], [2, 1], [3, 0], [0, 0], [3, 3]]
    points = [Point(0, 3), Point(2,2), Point(1,1), Point(2,1), Point(3,0), Point(0,0), Point(3,3)]
    n = len(points)
    convexHull(points, n)

25. gcd
# Basic Euclidean algorithms to gcd
def gcd(a, b):

    if a == 0:
        return b

    return gcd(b%a, a)

# Extend Euclidean algorithms to gcd
def gcdExtended(a, b):

    if a == 0:
        x = 0
        y = 1

        return x, y, b

    x1, y1, g = gcdExtended(b%a, a)
    x = y1 - (b/a) * x1
    y = x1

    return x, y, g

'''
5
5
1
(-1, 1, 5)
(1, -3, 5)
(1, -15, 1)
'''
if __name__ == "__main__":
    for i in [[10, 15], [35, 10], [31, 2]]:
        print gcd(i[0], i[1])

    for i in [[10, 15], [35, 10], [31, 2]]:
        print gcdExtended(i[0], i[1])

27. Print the pair with sum closest to x
def printClosest(arr, n, x):

    import sys

    # Initialize left and right indexes and difference 
    # between pair sum and x
    l = 0
    r = n - 1
    diff = sys.maxint

    # while there are elements between l and r
    while r > l:
        # check if this pair is closer than the closet pair so far
        if abs(arr[l] + arr[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l] + arr[r] - x )

        # if this pair has more sum, move to smaller values
        if arr[l] + arr[r] > x:
            r -= 1
        else:
            l += 1

    print 'Closest pair is: %s %s' % (arr[res_l], arr[res_r])

'''
Closest pair is: 22 30
'''
if __name__ == "__main__":
    arr = [10, 22, 28, 29, 30, 40]
    x = 54
    n = len(arr)
    printClosest(arr, n, x)

28. longest continuous sub sequence 
def lcs_continuous(a, b):

    m = len(a)
    n = len(b)

    num =  [[0]*(n+1) for _ in range(m+1)]

    maxlen = 0
    lastSubsBegin = 0
    maxSub = ''

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                if i == 0 or j == 0:
                    num[i][j] = 1
                else:
                    num[i][j] = 1 + num[i-1][j-1]
 
                if num[i][j] > maxlen:
                    maxlen = num[i][j]
                    thisSubsBegin = i - num[i][j] + 1
                    if lastSubsBegin == thisSubsBegin:
                        maxSub += a[i]
                    else:
                        lastSubsBegin = thisSubsBegin
                        maxSub = ''
                        maxSub += a[lastSubsBegin: i+1]
               
    return maxlen, maxSub

'''
(4, 'acad')
(3, 'aba')
(1, 'G')
'''
if __name__ == "__main__":
    ret = lcs_continuous('academy', 'abracadabra')
    print ret

    ret = lcs_continuous('ababc', 'abcdaba')
    print ret

    ret = lcs_continuous('GAGTAB', 'GXTXAYB')
    print ret

29. longest increasing subsequence
def longIncSub(arr):

    n = len(arr)
    tmpList = []
    
    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n

    # Compute optimized LIS values in bootom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Initialize maximum to 0 to get the maximum of all LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        if lis[i] > maximum:
            maximum = lis[i]
            tmpList.append(arr[i])

    return maximum, tmpList

'''
(5, [10, 22, 33, 50, 60])
'''
if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print longIncSub(arr)

30. Edit distance
# Edit distance problem
def editDistance(str1, str2):

    def editDistDP(str1, str2, m, n):
        # Create a table to store results of subproblems
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # Fill d[][] in bottom up manner
        for i in range(m+1):
            for j in range(n+1):
                # If first string is empty, only options is to 
                # insert all characters of second string
                if i == 0:
                    dp[i][j] = j

                # If second string is empty, only option is to 
                # remove all characters of second string
                elif j == 0:
                    dp[i][j] = j

                # If last characters are the same , ingore last char
                # and recur for remaining string
                elif str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                # If last character are different, consider all
                # possibilities and find minimum
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], # insert
                                       dp[i-1][j], # remove
                                       dp[i-1][j-1]) # replace

        return dp[m][n]

    m = len(str1)
    n = len(str2)

    return editDistDP(str1, str2, m, n)

'''
3
'''
if __name__ == "__main__":
    str1 = "sunday"
    str2 = "saturday"

    print editDistance(str1, str2)
    
31. partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
def findMinDP(arr):

    n = len(arr)

    # Calculate sum of all elements
    theSum = 0
    for i in range(n):
        theSum += arr[i]

    # Create an array to store results of subproblems
    dp = [[False]*(theSum+1) for _ in range(n+1)]

    # Initialize first column as true, 0 sum is possible
    # with all elements
    for  i in range(0, n+1):
        dp[i][0] = True

    # Initialize top row, except dp[0][0], as false
    # with 0 elements, no other sum except 0 is possible
    for i in range(1, theSum+1):
        dp[0][i] = False

    # Fill the partition table in bottom up manner
    for i in range(1, n+1):
        for j in range(1, theSum+1):
            # If ith element is excluded
            dp[i][j] = dp[i-1][j]

            # If ith element is included
            if arr[i-1] <= j:
                dp[i][j] |= dp[i-1][j-arr[i-1]]

    # Initialize difference of two sums
    import sys
    diff = sys.maxint

    # Find the largest j such that dp[n][j]
    # is true where j loops from sum/2 to 0
    for j in range(theSum/2, -1, -1):
        if dp[n][j] == True:
            print 'j:', j
            diff = theSum - 2*j
            break

    return diff

if __name__ == "__main__":
    arr = [3, 1, 4, 2, 2, 1]
    print findMinDP(arr)
    arr = [1, 6, 11, 5]
    print findMinDP(arr)

32. Count number of ways to cover a distance
#A naive recursive program to count number of ways to cover
#a distance with 1, 2 and 3 steps
def printCountRec(dist):

    # Base cases
    if dist < 0:
        return 0
    elif dist == 0:
        return 1

    # Recur for all previous 3 and add the results
    return printCountRec(dist-1) + \
           printCountRec(dist-2) + \
           printCountRec(dist-3)

#A Dynamic Programming based program to count number of ways
#to cover a distance with 1, 2 and 3 steps
def printCountDP(dist):

    count = [None] * (dist+1)

    # Initialize base values 
    # one way to cover 0 and 1 distance
    # two ways to cover 2 distance
    count[0] = 1
    count[1] = 1
    count[2] = 2

    # Fill the count array in bottom up manner
    for i in range(3, dist+1):
        count[i] = count[i-1] + count[i-2] + count[i-3]

    return count[dist]

'''
4
4
149
149
'''
if __name__ == "__main__":
    for dist in [3, 9]:
        print printCountRec(dist)
        print printCountDP(dist)    

33. rod cutting
def curRod(n, pList):

    N = 1000
    pList = pList
    rList = [-1 for _ in range(N)]
    sList = [None] * N
    rList[0] = 0

    # naive exponential soluation
    def curRodNv(n):
        q = 0
        for i in range(1, n+1):
            q = max(q, pList[i]+curRodNv(n-i))

        return  q

    # bottomUp soluation that maintains not only the best
    # price but also the required cut for such solution
    def extendedBottomUpCutRod(n):
        if rList[n] != -1:
            return rList[n]

        for j in range(1, n+1):
            q = 0
            for i in range(1, j+1):
                if q < pList[i] + rList[j -i]:
                    q = pList[i] + rList[j-i]
                    sList[j] = i
            rList[j] = q

        return rList[n]

    # print the extended method output
    def printCutRodSol(n):
        while True:
            print sList[n]
            
            n -= sList[n]
            if n <= 0:
                break

    print extendedBottomUpCutRod(n)
    printCutRodSol(n)

'''
22
2
6
'''
if __name__ == "__main__":
    pList = [0,1,5,8,9,10,17,17,20,24,30]
    n = 8
    curRod(n, pList)

34. Find the longest path in a matrix with given constraints
# define n
n = 3

# Returns length of the longest path beginning with mList[i][j]
# This function mainly uses lookup table dp[n][n]
def findLongestFromACell(i, j, mList, dp):

    # Base case
    if i < 0 or i >= n or j < 0 or j >= n:
        return 0

    # If this subproblem is already solved
    if dp[i][j] != -1:
        return dp[i][j]

    # Since all numbers are unique and in range from 1 to n*n
    # there is atmost one possible direction from any cell
    if j < n-1 and (mList[i][j] + 1) == mList[i][j+1]:
        dp[i][j] = 1 + findLongestFromACell(i, j+1, mList, dp)
        return dp[i][j]

    if j > 0 and (mList[i][j] + 1) == mList[i][j-1]:
        dp[i][j] = 1 + findLongestFromACell(i, j-1, mList, dp)
        return dp[i][j]

    if i > 0 and (mList[i][j] + 1) == mList[i-1][j]:
        dp[i][j] = 1 + findLongestFromACell(i-1, j, mList, dp)
        return dp[i][j]

    if i < n-1 and (mList[i][j] + 1) == mList[i+1][j]:
        dp[i][j] = 1 + findLongestFromACell(i+1, j, mList, dp)
        return dp[i][j]

    # If none of the adjacent fours is one greater
    dp[i][j] = 1
    return dp[i][j]

# Returns length of the longest path beginning with any cell
'''
Given a n*n matrix where numbers all numbers are distinct and are distributed from range 1 to n2, 
find the maximum length path (starting from any cell) such that all cells along the path are increasing order with a difference of 1.
'''
def finLongestOverAll(mList):

    # Initialize result
    result = 1

    # Create a lookup table and fill all entries in it as -1
    dp = [[-1] * n for _ in range(n)]

    # Compute longest path beginning from all cells
    for i in range(0, n):
        for j in range(0, n):
            if dp[i][j] == -1:
                findLongestFromACell(i, j, mList, dp)

            # Update result if needed
            result = max(result, dp[i][j])

    return result

'''
4
'''
if __name__ == "__main__":
    mList = [[1,2,9],
             [5,3,8],
             [4,6,7]]
    mList = [[3,4,5],
             [3,2,6],
             [2,2,1]]
    print finLongestOverAll(mList)

35. subsetSum
def subsetSum(nList, target, partial=[]):

    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print "sum(%s)=%s" % (partial, target)
    if s >= target:
        return

    for i in range(len(nList)):
        n = nList[i]
        remaining = nList[i+1:]
        subsetSum(remaining, target, partial+[n])

'''
sum([2, 6, -1, 1, 7])=15
sum([2, 6, 7])=15
sum([2, 8, 1, 4])=15
sum([2, 9, -1, 1, 4])=15
sum([2, 9, 4])=15
sum([2, -1, 1, 13])=15
sum([2, 1, 12])=15
sum([2, 13])=15
sum([6, 8, 1])=15
sum([6, 9])=15
sum([14, 1])=15
sum([8, -1, 1, 7])=15
sum([8, 7])=15
sum([9, -1, 7])=15
sum([15])=15
sum([-1, 12, 4])=15
sum([-1, 16])=15
'''
if __name__ == "__main__":
    subsetSum([2,6,14,8,9,15,-1,1,24,12,4,20,13,7,16],15)

36. knapsack
import collections
import functools

class Memoized:
    '''
    Decorator, caches a function's return value each item it is called
    If called later with the same arguments, the cached value is returned
    (not reevaluated).
    '''
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if not isinstance(args, collections.Hashable):
            # uncacheable, a list, for instance
            # better to not cache than blow up
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            value = self.func(*args)
            self.cache[args] = value
            return value
    def __repr__(self):
        '''Return the funciton's docstring.'''
        return self.func.__doc__

    def __get__(self, obj, objtype):
        '''Support instance methods'''
        return functools.partial(self.__call__, obj)

def knapsack(items, maxweight):
    """
    Solve the knapsack problem by finding the most valuable
    subsequence of items subject that weights no more than
    maxweight

    items is s sequence of pairs (value, weight) where value if
    a number and weight is a non-negative integer.

    maxweight is a non-negative integer.

    return a pair whose first element is the sum of values in the most
    valuable subsequence, and whose second elements is the subsequence.

    >>> items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
    >>> knapsack(items, 15)
    (11, [(2, 1), (6, 4), (1, 1), (2, 2)])
    """

    # Returns the value of the most valuable subsequence of the first i
    # elements in items whose weights sum to no more than j
    @Memoized
    def bestvalue(i, j):
        if i == 0: return 0
        value, weight = items[i-1]
        if weight > j:
            return bestvalue(i-1, j)
        else:
            return max(bestvalue(i-1, j),
                 bestvalue(i-1, j-weight)+value)

    j = maxweight
    result = []
    for i in xrange(len(items), 0, -1):
        if bestvalue(i, j) != bestvalue(i-1,j):
            result.append(items[i-1])
            j -= items[i-1][1]
    result.reverse()
    return bestvalue(len(items), maxweight), result

'''
(11, [(2, 1), (6, 4), (1, 1), (2, 2)])
'''
if __name__ == "__main__":
    items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
    print knapsack(items, 15)

    '''
37. Minimum Initial Energy Required To Cross Street
Given an array containing positive and negative numbers.
The array represents checkpoints from one end to other end of street.
Positive and negative values represent amount of energy at that checkpoint.
Positive numbers increase the energy and negative numbers decrease.
Find the minimum initial energy required to cross the street such that Energy level never becomes 0 or less than 0.

Note : The value of minimum initial energy required will be 1 even
if we cross street successfully without loosing energy to less than and equal to 0 at any checkpoint.
The 1 is required for initial check point.

Examples:

Input : arr[] = {4, -10, 4, 4, 4}
Output: 7
Suppose initially we have energy = 0, now at 1st
checkpoint, we get 4. At 2nd checkpoint, energy gets
reduced by -10 so we have 4 + (-10) = -6 but at any
checkpoint value of energy can not less than equals
to 0. So initial energy must be at least 7 because
having 7 as initial energy value at 1st checkpoint
our energy will be = 7+4 = 11 and then we can cross
2nd checkpoint successfully. Now after 2nd checkpoint,
all checkpoint have positive value so we can cross
street successfully with 7 initial energy.

Input : arr[] = {3, 5, 2, 6, 1}
Output: 1
We need at least 1 initial energy to reach first
checkpoint

Input : arr[] = {-1, -5, -9}
Output: 16
We take initial minimum energy 0 i.e; initMinEnergy = 0 and energy at any checkpoint as currEnergy = 0.
Now traverse each checkpoint linearly and add energy level at each i’th checkpoint i.e; currEnergy = currEnergy + arr[i].
If currEnergy becomes non-positive, then we need at least “abs(currEnergy) + 1″ extra initial energy to cross this point. 
Therefore we update initMinEnergy = (initMinEnergy + abs(currEnergy) + 1). 
We also update currEnergy = 1 as we now have the required extra minimum initial energy for next point.
'''
def minInitialEnery(arr):

    # get the length
    n = len(arr)

    # initMinEnergy is variable to store minimum inital 
    # energy required
    initMinEnergy = 0

    # currEnergy is variable to store current value of 
    # energe at ith checkpoint on street
    currEnergy = 0

    # flag to check if we have successfully crossed the 
    # street without any energy loss <= 0 at any checkpoint
    flag = 0

    # Traverse each check point linerally
    for i in range(0, n):
        currEnergy += arr[i]

        # If current energy, becomes negative or 0, increment
        # initial mimimum energy by the negative value plus 1
        # to keep current energy positive (at least 1)
        # Also update current energy and flag
        if currEnergy <= 0:
            initMinEnergy += abs(currEnergy) + 1
            currEnergy = 1
            flag = 1

    # If energy never became nagative or 0, then return 1
    # Else return computed initMinEnergy
    if flag == 0:
        return 1
    else:
        return initMinEnergy

if __name__ == "__main__":
    for arr in [[4, -10, 4, 4, 4], [3, 5, 2, 6, 1], [-1, -5, -9]]:
        print minInitialEnery(arr)
