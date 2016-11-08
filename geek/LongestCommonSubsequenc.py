'''
Longest common subsequence with permutations allowed

Given two strings in lowercase, find the longest string whose permutations 
are subsequences of given two strings. The output longest string must be sorted.

Examples:

Input  :  str1 = "pink", str2 = "kite"
Output : "ik" 
The string "ik" is the longest sorted string 
whose one permutation "ik" is subsequence of
"pink" and another permutation "ki" is 
subsequence of "kite". 

Input  : str1 = "working", str2 = "women"
Output : "now"

Input  : str1 = "geeks" , str2 = "cake"
Output : "ek"

Input  : str1 = "aaaa" , str2 = "baba"
Output : "aa"
'''
def longestString(aStr1, aStr2):

    # init
    count1 = {i:0 for i in range(26)}
    count2 = {i:0 for i in range(26)}

    # get the length
    n1 = len(aStr1)
    n2 = len(aStr2)

    # calculate frequency of characters
    for i in range(n1):
        count1[ord(aStr1[i])-ord('a')] += 1

    for i in range(n2):
        count2[ord(aStr2[i])-ord('a')] += 1

    # traverse hasy array
    result = ''
    for i in range(26):
        # append character ('a' + i) in result
        # string result by min(count1[i],count2[i]) times
        for _ in range(1, min(count1[i],count2[i])+1):
            result += chr(ord('a')+i)

    print result

'''
ik
now
ek
aa
'''
if __name__ == "__main__":
    aStr1 = "pink"
    aStr2 = "kite"
    longestString(aStr1, aStr2)
    
    aStr1 = "working"
    aStr2 = "women"
    longestString(aStr1, aStr2)
    
    aStr1 = "geeks" 
    aStr2 = "cake"
    longestString(aStr1, aStr2)
    
    aStr1 = "aaaa" 
    aStr2 = "baba"
    longestString(aStr1, aStr2)
