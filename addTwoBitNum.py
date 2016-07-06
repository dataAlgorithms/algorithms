def addBit(aList, bList):

    assert len(aList) == len(bList),"not equal."
    n = len(aList)
    cList = [0] * (n+1)

    flag = 0
    for i in range(n, 0, -1):
        cList[i] = aList[i-1] + bList[i-1] + flag
        if cList[i] > 1:
            cList[i] = cList[i] % 2
            flag = 1
        else:
            flag = 0

    cList[0] = flag
    for i in range(0, n+1):
        print cList[i],

if __name__ == "__main__":
    aList = [1,0,1,1,0,1,1,1]
    bList = [0,1,1,0,0,1,0,1]
    addBit(aList, bList)    
