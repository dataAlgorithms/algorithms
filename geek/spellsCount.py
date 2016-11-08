'''
Count ways to spell a number with repeated digits
Given a string that contains digits of a number.
The number may contain many same continuous digits in it.
The task is to count number of ways to spell the number.

Examples:

Input :  num = 100
Output : 2
The number 100 has only 2 possibilities,
1) one zero zero
2) one double zero.

Input : num = 11112
Output: 8
1 1 1 1 2, 11 1 1 2, 1 1 11 2, 1 11 1 2
11 11 2, 1 111 2, 111 1 2, 1111 2

Input : num = 12345
Output: 1

Input : num = 11111
Output: 16

This is a simple problem of permutation and combination. 
If we take example test case given in the question, 11112. 
The answer depends on the number of possible combinations of 1111. 
The number of combinations of “1111” is 2^3 = 8. As our combinations will 
depend on whether we choose a particular 1 and for “2” there will be only 
one possibility 2^0 = 1, so answer for “11112” will be 8*1 = 8.
So, the approach is to count the particular continuous digit 
in string and multiply 2^(count-1) with previous result.
'''
def spellsCount(strNum):

    # get the length
    n = len(strNum)

    # final count of total possible spells
    result = 1

    # iterate through complete number
    i = 0
    while i < n:
        # count contiguous frequency of particular
        # digit num[i]
        count = 1
        while i < n-1 and strNum[i+1] == strNum[i]:
            count += 1
            i += 1

        # compute 2^(count-1) and multiply with result
        result = result * pow(2, count-1)

        i += 1

    return result

'''
16
1
8
'''
if __name__ == "__main__":
    for strNum in ['11111', '12345', '11112']:
        print spellsCount(strNum)
