def printAllKLength(sList, k):

    n = len(sList)
    printAllKLengthRec(sList, "", n, k)

def printAllKLengthRec(sList, prefix, n, k):

    # Base case: k is 0, print prefix
    if (k == 0):
        print(prefix)
        return

    # One by one add all characters from sList and recursively
    # call for k equals to k-1
    for i in range(0, n):
        # next character of input added
        newPrefix = prefix + sList[i]

        # k is decreased, because we have added a new character
        printAllKLengthRec(sList, newPrefix, n, k-1)

def main():

    sList = ['a', 'b']
    k = 3
    printAllKLength(sList, k)
	
    print("\r")
	
    sList = ['a', 'b', 'c', 'd']
    k = 1
    printAllKLength(sList, k)

'''
aaa
aab
aba
abb
baa
bab
bba
bbb

a
b
c
d
'''
if __name__ == "__main__":
    main()
