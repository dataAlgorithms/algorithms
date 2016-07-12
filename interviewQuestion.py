1. Reverse a string
def reverse_string(aString=None):

    if aString is None:
        return

    aString = [s for s in aString]

    n = len(aString)
    i = 0
    j = n-1
    while i < n/2:
        aString[i],aString[j]=aString[j],aString[i]
        i += 1
        j -= 1

    aString = ''.join(aString)

    print aString

if __name__ == "__main__":
    aString = "Ab,c,de!$"
    reverse_string(aString)

if __name__ == "__main__":
    aString = "Ab,c,de!$"
    print 'Primary string:', aString
    print '\rReverse string:'
    reverse_string(aString)
