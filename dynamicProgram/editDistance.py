'''
Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations. 
Replace 'n' with 'r', insert t, insert a
'''

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
