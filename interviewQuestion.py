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
