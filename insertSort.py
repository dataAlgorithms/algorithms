'''
1.  Insert sort

 O(n*n)
'''
def insertSort(theSeq):
    
    # Get the length
    n = len(theSeq)
    
    # Do the loop
    for i in range(1, n):
        pos = i
        pivot = theSeq[pos]
        while pos > 0 and pivot < theSeq[pos-1]:
            theSeq[pos] = theSeq[pos-1]
            pos -= 1

        theSeq[pos] = pivot

'''
[-3, -1, 0, 1, 3, 6, 20]
'''
if __name__ == "__main__":

    theSeq = [-1, -3, 0, 1, 6, 3, 20]
    insertSort(theSeq)
    print theSeq
    
'''
2. Head sorted linked list 
(including insert item into sorted linked list)
'''
# Implement Bag using linked list
class HeadSortedLinkedListBag:
    # Init
    def __init__(self):
        self._head = None
        self._size = 0

    # Length
    def __len__(self):
        return self._size

    # Contain
    def __contains__(self, target):
        curNode = self._head
        while curNode is not None and curNode.data <= target:
            if curNode.data == target:
                return True
            else:  
                curNode = curNode.next

        return False

    # Add (insert item into sorted linked list)
    def add(self, element):
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.data < element:
            preNode = curNode
            curNode = curNode.next

        newItem = LinkedListBagElement(element)
        newItem.next = curNode
        if curNode is self._head:
            self._head = newItem
        else:
            preNode.next = newItem

        self._size += 1

    # Remove
    def remove(self, element):
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.data != element:
            preNode = curNode
            curNode = curNode.next

        assert curNode is not None, "element is not in the Bag."
        self._size -= 1

        if curNode is self._head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next

        return curNode.data

    # Iter
    def __iter__(self):
        return LinkedListBagIterator(self._head)

# Bag storage
class LinkedListBagElement:
    # Init
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Bag iter
class LinkedListBagIterator:
    # Init
    def __init__(self, head):
        self.curNode = head
    def __iter__(self):
        return self
    def next(self):
        if self.curNode is not None:
            value = self.curNode.data
            self.curNode = self.curNode.next
            return value
        else:
            raise StopIteration
        
def test_linkedListBag():
    
    # init a set named smith
    smith = HeadSortedLinkedListBag()
    smith.add('CSCI-112')
    smith.add('MATH-121')
    smith.add('HIST-340')
    smith.add('ECON-101')
    
    print 'smith: '
    for item in smith:
        print item,
    
    # init a set named roberts
    roberts = HeadSortedLinkedListBag()
    roberts.add('POL-101')
    roberts.add('ANTH-230')
    roberts.add('CSCI-112')
    roberts.add('ECON-101')
    
    print '\r\rroberts: '
    for item in roberts:
        print item,
        
    print '\r\rremove ECON-101 of smith'
    smith.remove('ECON-101')

    print '\r\rsmith: '
    for item in smith:
        print item,
        
    print '\r\rremove MATH-121 of smith'
    smith.remove('MATH-121')
            
    print '\r\rsmith: '
    for item in smith:
        print item,
        
    print '\r\rin check'
    print 'HIST-340' in smith 
    print 'MATH-121' in smith
 
'''
smith: 
CSCI-112 ECON-101 HIST-340 MATH-121 

roberts: 
ANTH-230 CSCI-112 ECON-101 POL-101 

remove ECON-101 of smith


smith: 
CSCI-112 HIST-340 MATH-121 

remove MATH-121 of smith


smith: 
CSCI-112 HIST-340 

in check
True
False

'''   
if __name__ == "__main__":
    test_linkedListBag()
