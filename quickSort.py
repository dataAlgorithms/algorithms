#! coding=utf-8

'''
1. quickSort (use last item as pivot)
'''

def quickSort(theSeq):

    def recQuickSort(theSeq, first, last):
    
        if first >= last:
            return
        else:
            pos = partitionSeq(theSeq, first, last)
            recQuickSort(theSeq, first, pos-1)
            recQuickSort(theSeq, pos+1, last)
    
    
    def partitionSeq(theSeq, first, last):
    
        x = theSeq[last]
        i = first - 1
    
        for j in range(first, last):
            if theSeq[j] <= x:
                i += 1
                theSeq[i],theSeq[j] = theSeq[j],theSeq[i]
    
        theSeq[i+1],theSeq[last] = theSeq[last],theSeq[i+1]
    
        return i+1
    
    n = len(theSeq)
    recQuickSort(theSeq, 0, n-1)
    
    
'''
2. quickSort ( use the first item as pivot)
'''
def quickSortNew(theSeq):

    def recQuickSort(theSeq, first, last):
    
        if first >= last:
            return
        else:
            pos = partitionSeqNew(theSeq, first, last)
            recQuickSort(theSeq, first, pos-1)
            recQuickSort(theSeq, pos+1, last)
    
    def partitionSeqNew(theSeq, first, last):
        
        pivot = theSeq[first]
        left = first + 1
        right = last 
        
        while left <= right:
            while left <= right and theSeq[left] <= pivot:
                left += 1
                
            while right >= left and theSeq[right] >= pivot:
                right -= 1
                
            if left < right:
                theSeq[left], theSeq[right] = theSeq[right], theSeq[left]
                
        theSeq[first] = theSeq[right]
        theSeq[right] = pivot
        
        return right
    
    n = len(theSeq)
    recQuickSort(theSeq, 0, n-1)
  
'''
3. quick sort (Reducing worst case space to Log n)
'''
  
def quickSortOpt(aList, low, high):

    def partitionSeq(theSeq, first, last):
    
        x = theSeq[last]
        i = first - 1
    
        for j in range(first, last):
            if theSeq[j] <= x:
                i += 1
                theSeq[i],theSeq[j] = theSeq[j],theSeq[i]
    
        theSeq[i+1],theSeq[last] = theSeq[last],theSeq[i+1]
    
        return i+1

    while low < high:
        #pi is partitioning index, arr[p] is now at right place
        pi = partitionSeq(aList, low, high)

        # If left part is smaller, then recur for left
        # part and handle right part iteratively
        if pi - low < high - pi:
            quickSortOpt(aList, low, pi-1)
            low = pi + 1
        else:
            # Else recur for right part
            quickSortOpt(aList, pi+1, high)
            high = pi - 1
            
'''
aList (sorted before): [69, 71, 86, 41, 66, 1, 66, 64, 37, 75, 5, 92, 48, 49, 88, 45, 56, 46, 1, 99]
aList (sorted after): [1, 1, 5, 37, 41, 45, 46, 48, 49, 56, 64, 66, 66, 69, 71, 75, 86, 88, 92, 99]

bList (new sorted before): [69, 71, 86, 41, 66, 1, 66, 64, 37, 75, 5, 92, 48, 49, 88, 45, 56, 46, 1, 99]
bList (new sorted after): [1, 1, 5, 37, 41, 45, 46, 48, 49, 56, 64, 66, 66, 69, 71, 75, 86, 88, 92, 99]

cList (optimize sorted before): [69, 71, 86, 41, 66, 1, 66, 64, 37, 75, 5, 92, 48, 49, 88, 45, 56, 46, 1, 99]
cList (optimize sorted after): [1, 1, 5, 37, 41, 45, 46, 48, 49, 56, 64, 66, 66, 69, 71, 75, 86, 88, 92, 99]
'''
if __name__ == "__main__":
    
    import random
    aList = [random.randrange(100) % 100 for _ in range(20)]
    bList = [item for item in aList]
    cList = [item for item in aList]
    
    print 'aList (sorted before):', aList
    quickSort(aList)
    print 'aList (sorted after):', aList       
    
    print ''
    print 'bList (new sorted before):', bList
    quickSort(bList)
    print 'bList (new sorted after):', bList         
    
    print ''
    print 'cList (optimize sorted before):', cList
    quickSort(cList)
    print 'cList (optimize sorted after):', cList       
