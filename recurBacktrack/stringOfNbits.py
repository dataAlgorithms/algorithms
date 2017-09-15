'''
1. Using recursive way

generate all strings of n bits by using recursive backtracking method..
 For example if given size of an array is 3 then the output should be 
[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,10] and [1,1,1].
'''
def allStringOfNbits(n):

    if n < 1:
        print(aList);
    else:
        aList[n-1] = '0'
        allStringOfNbits(n-1);
        aList[n-1] = '1'
        allStringOfNbits(n-1)
'''
['0', '0', '0', '0']
['1', '0', '0', '0']
['0', '1', '0', '0']
['1', '1', '0', '0']
['0', '0', '1', '0']
['1', '0', '1', '0']
['0', '1', '1', '0']
['1', '1', '1', '0']
['0', '0', '0', '1']
['1', '0', '0', '1']
['0', '1', '0', '1']
['1', '1', '0', '1']
['0', '0', '1', '1']
['1', '0', '1', '1']
['0', '1', '1', '1']
['1', '1', '1', '1']
'''
if __name__ == "__main__":
    n = 4
    aList = [None] * n
    allStringOfNbits(n)
    
'''
2. Using non-recursive way

#!/usr/bin/env python
# -*- coding:utf-8 -*-

n-bit Gray Codes can be generated from list of (n-1)-bit Gray codes using following steps.
1) Let the list of (n-1)-bit Gray codes be L1. Create another list L2 which is reverse of L1.
2) Modify the list L1 by prefixing a ‘0’ in all codes of L1.
3) Modify the list L2 by prefixing a ‘1’ in all codes of L2.
4) Concatenate L1 and L2. The concatenated list is required list of n-bit Gray codes.

For example, following are steps for generating the 3-bit Gray code list from the list of 2-bit Gray code list.
L1 = {00, 01, 11, 10} (List of 2-bit Gray Codes)
L2 = {10, 11, 01, 00} (Reverse of L1)
Prefix all entries of L1 with ‘0’, L1 becomes {000, 001, 011, 010}
Prefix all entries of L2 with ‘1’, L2 becomes {110, 111, 101, 100}
Concatenate L1 and L2, we get {000, 001, 011, 010, 110, 111, 101, 100}

To generate n-bit Gray codes, we start from list of 1 bit Gray codes. The list of 1 bit Gray code is {0, 1}. 
We repeat above steps to generate 2 bit Gray codes from 1 bit Gray codes, then 3-bit Gray codes from 2-bit 
Gray codes till the number of bits becomes equal to n. 
'''
def generateGrayArr(n):

    # base case
    if n <= 0:
        return

    # aList will store all genereated codes
    aList = []

    # start with one-bit pattern
    aList.append('0')
    aList.append('1')

    # Every iteration of this loop generates 2*i codes from
    # previously generated i codes
    i = 2
    while i < (1 << n):

        # Enter the previously generated codes again in aList in
        # reverse order, Nor aList[] has double number of codes
        j = i - 1
        while j >= 0:
            aList.append(aList[j])
            j = j -1

        # append 0 to the first half
        j = 0
        while j < i:
            aList[j] = "0" + aList[j]
            j = j + 1

        # append 1 to the second half
        j = i
        while j < 2 * i:
            aList[j] = "1" + aList[j]
            j = j + 1

        i = i << 1

    # print content of aList
    for i in range(0, len(aList)):
        print(aList[i])

'''
0000
0001
0011
0010
0110
0111
0101
0100
1100
1101
1111
1110
1010
1011
1001
1000
'''
if __name__ == "__main__":
    n = 4
    generateGrayArr(n)
    
