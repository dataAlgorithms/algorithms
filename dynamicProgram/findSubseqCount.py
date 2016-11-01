#! coding=utf-8 

'''
Count distinct occurrences as a subsequence
Given a two strings S and T, find count of distinct occurrences of T in S as a subsequence.

Examples:

Input  : S = banana, T = ban
Output : 3
T appears in S as below three subsequences.
[ban], [ba  n], [b   an]

Input  : S = geeksforgeeks, T = ge
Output : 6
T appears in S as below three subsequences.
[ge], [     ge], [g e], [g    e] [g     e]
and [     g e]

This problem can be recursively defined as below.

// Returns count of subsequences of S that match T
// m is length of T and n is length of S
subsequenceCount(S, T, n, m)

   // An empty string is subsequence of all.
   1) If length of T is 0, return 1.

   // Else no string can be a sequence of empty S.
   2) Else if S is empty, return 0.

   3) Else if last characters of S and T don't match,
      remove last character of S and recur for remaining
        return subsequenceCount(S, T, n-1, m)

   4) Else (Last characters match), the result is sum
      of two counts.

        // Remove last character of S and recur.
        a) subsequenceCount(S, T, n-1, m) +

        // Remove last characters of S and T, and recur.
        b) subsequenceCount(S, T, n-1, m-1)

Since there are overlapping subproblems in above recurrence result,
we can apply dynamic programming approach to solve above problem.
We create a 2D array mat[m+1][n+1] where m is length of string T and n
is length of string S. mat[i][j] denotes the number of distinct subsequence
of substring S(1..i) and substring T(1..j) so mat[m][n] contains our solution.
'''
def findSubsequenceCount(sStr, tStr):

    # get the length
    n = len(sStr)
    m = len(tStr)

    # T cannot appear as a subsequence in S
    if m > n:
        return 0

    # mat[i][j] stores the count of occurences of 
    # T(1..i) in S(1..j)
    mat = [[0] * (n+1) for _ in range(m+1)]

    # Initializing first column with all 0s. An empty
    # string cannot have another string as subsequence
    for i in range(1, m+1):
        mat[i][0] = 0

    # Initializing first row with all 1s. An empty
    # string is subsequence of all
    for j in range(0, n+1):
        mat[0][j] = 1

    # Fill mat in bottom up manner
    for i in range(1, m+1):
        for j in range(1, n+1):
            # If last characters donot match, then value
            # is same as the value without last character in S
            if tStr[i-1] != sStr[j-1]:
                mat[i][j] = mat[i][j-1]

            # Else value is obtained considering two cases
            # a) All substrings without last character in S
            # b) All substrings without last character in both
            else:
                mat[i][j] = mat[i][j-1] + mat[i-1][j-1]
                
    return mat[m][n]

'''
6
3
'''
if __name__ == "__main__":
    tStr = "ge";
    sStr = "geeksforgeeks"
    print findSubsequenceCount(sStr, tStr)
    
    tStr = "ban";
    sStr = "banana"
    print findSubsequenceCount(sStr, tStr)
