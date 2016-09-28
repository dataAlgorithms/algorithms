# longest continuous sub sequence 
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
