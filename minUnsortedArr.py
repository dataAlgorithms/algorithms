#! coding=utf-8 

'''
1. find minimum unsorted array
'''
def minimumUnSorted(theSeq):

    # get the length 
    n = len(theSeq)

    # find the first left item which is above then the follow item
    for s in range(0, n-1):
        if theSeq[s] > theSeq[s+1]:
            break

    if s == n-1:
        print 'theSeq is already sorted.!'
        return

    # find the first right item which is less than the before item
    for e in range(n-2, 0, -1):
        if theSeq[e] < theSeq[e-1]:
            break

    # find the min and max between s and e
    theMin = theSeq[s]
    theMax = theSeq[e]
    for k in range(s+1, e+1):
        if theSeq[k] < theMin:
            theMin = theSeq[k]

        if theSeq[k] > theMax:
            theMax = theSeq[k]

    # check value for s
    for i in range(0, s):
        if theSeq[i] > theMin:
            s = i
            break

    # check value of e
    for j in range(n-1, e, -1):
        if theSeq[j] < theMax:
            e = j
            break

    return s, e

'''
start= 3 end= 8
[30, 25, 40, 32, 31, 35]
'''
if __name__ == "__main__":
    theSeq = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
    start,end = minimumUnSorted(theSeq)
    print "start=",start,"end=",end
    print theSeq[start:end+1]
