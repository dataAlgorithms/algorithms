'''
Count Substrings with equal number of 0s, 1s and 2s
Given a string which consists of only 0s, 1s or 2s, 
count the number of substrings that have equal number of 0s, 1s and 2s.

Examples:

Input  :  str = "0102010"
Output :  2
Explanation : 
102 201 

Input : str = "102100211"
Output : 5
Explaination: 
102 021 210 021 210021 

A simple solution is to iterate through all substring of str and checking whether 
they contain equal 0,1 and 2 or not. Total number of substring of str is O(n2) 
checking each substring for count takes O(n) times, So total 
time takedn to solve this problem is O(n3) time with brute-force approach.

An efficient solution is to keep track of counts of 0, 1 and 2.

Let zc[i] denotes number of zeros between index 1 and i
    oc[i] denotes number of ones between index 1 and i
    tc[i] denotes number of twos between index 1 and i
for substring str[i, j] to be counted in result we should have :
    zc[i] - zc[j-1] = oc[i] - oc[j-1] = tc[i] - tc[j-1]
we can write above relation as follows :
z[i] -o[i] = z[j-1] - o[j-1]    and
z[i] -t[i] = z[j-1] - t[j-1]
The above relations can be tracked while looping in string, at each index i we'll 
calculate this difference pair and we'll check how many time this difference pair has
 previously occurred and we'll add that count to our result, for keeping track of previous
  difference pair we have used map in below code. Total time complexity of this solution is
   O(n log n) considering the fact that map operations, 
   like search and insert take O(Log n) time.
'''
# Count number of substring which
# has equal o, 1 and 2
def getSubstringWithEquql012(aStr):

    # get the length
    n = len(aStr)

    # map to store, how many times a difference
    # pair has occurred previously
    mp = {}
    mp[(0,0)] = 1

    # zc (Count of zeroes), oc(Count of 1s)
    # and tc(count of twos)
    # In starting all counts are zero
    zc = 0
    oc = 0
    tc = 0

    # looping into string
    res = 0
    for i in range(0, n):
        # increasing the count of current character
        if aStr[i] == '0':
            zc += 1
        elif aStr[i] == '1':
            oc += 1
        elif aStr[i] == '2':
            tc += 1

        # make pair of differences (z[i] - o[i],
        # z[i] - t[i]
        tmp = (zc-oc, zc-tc)

        # Count of previous occurrences of above pair
        # indicates that the subarrays forming from
        # every previous occurence to this occurrence
        # is a subarray with equal number of 0s,1s,and 2s
        if not mp.has_key(tmp):
            mp[tmp] = 0
            
        res = res + mp[tmp]

        # increasing the count of current difference
        # pair by 
        mp[tmp] += 1

    return res

'''
0
2
5
1
'''
if __name__ == "__main__":
    for aStr in ["111","0102010", "102100211","012"]:
        print getSubstringWithEquql012(aStr)
