# longest not continuous sub sequence 
def lcs_not_continuous(a, b):

    m = len(a)
    n = len(b)

    num =  [[0]*(n+1) for _ in range(m+1)]

    maxlen = 0
    lastSubsBegin = 0
    maxSub = ''

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                num[i][j] = 0
            elif a[i-1] == b[j-1]:
                num[i][j] = 1 + num[i-1][j-1]
            else:
                if num[i-1][j] > num[i][j-1]:
                    num[i][j] = num[i-1][j]
                else:
                    num[i][j] = num[i][j-1]

    # num[m][n] contains length of LCS for a[0..n-1] and b[0..m-1]              
    return num[m][n]

'''
4
3
'''
if __name__ == "__main__":
    ret = lcs_not_continuous('AGGTAB', 'GXTXAYB')
    print ret

    ret = lcs_not_continuous('ABCDGH', 'AEDFHR')
    print ret
