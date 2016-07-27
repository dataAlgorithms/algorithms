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
