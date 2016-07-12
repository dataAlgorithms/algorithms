1. Reverse a string
def reverse_string(aString=None):

    if aString is None:
        return

    n = len(aString)
    aTmp = ''
    for iStr in range(n-1, -1, -1):
        aTmp += aString[iStr]

    print aTmp

if __name__ == "__main__":
    aString = "Ab,c,de!$"
    print 'Primary string:', aString
    print '\rReverse string:'
    reverse_string(aString)
