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

2. reverse string without affecting special character
eg. 
Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"
def reverse_string_without_affect_special_character(aString=None):

    if aString is None:
        return

    aString = [s for s in aString]

    n = len(aString)
    i = 0
    j = n-1
    while i < j:
        if not aString[i].isalnum():
            i += 1
            continue
        if not aString[j].isalnum():
            j -= 1
            continue

        aString[i],aString[j]=aString[j],aString[i]
        i += 1
        j -= 1

    aString = ''.join(aString)

    print aString
