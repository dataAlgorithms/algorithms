# linear search 
def linearSearch(theSeq, target):

    # get the length
    n = len(theSeq)

    # do loop
    for i in range(n):
        if target == theSeq[i]:
            return i

    return -1

'''
theSeq: [1, 2, 12, 7, 19, 14, 6, 15, 17, 13, 0, 16, 4, 11, 9, 8, 5, 18, 10, 3]
7
-1
'''
if __name__ == "__main__":
    import random
    theSeq = range(20)
    random.shuffle(theSeq)

    print 'theSeq:', theSeq
    target = 15
    print linearSearch(theSeq, target) 

    target = 150
    print linearSearch(theSeq, target) 
