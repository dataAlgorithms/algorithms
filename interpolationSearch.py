'''
Interpolation Search
Given a sorted array of n uniformly distributed values arr[],
write a function to search for a particular element x in the array.

Linear Search finds the element in O(n) time,
Jump Search takes O(√ n) time and Binary Search take O(Log n) time.
The Interpolation Search is an improvement over Binary Search for instances,
where the values in a sorted array are uniformly distributed. Binary Search always goes to middle element to check.
On the other hand interpolation search may go to different locations according the value of key being searched.
For example if the value of key is closer to the last element, interpolation search is likely to start search toward the end side.

To find the position to be searched, it uses following formula.

// The idea of formula is to return higher value of pos
// when element to be searched is closer to arr[hi]. And
// smaller value when closer to arr[lo]
pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

arr[] ==> Array where elements need to be searched
x     ==> Element to be searched
lo    ==> Starting index in arr[]
hi    ==> Ending index in arr[]
Algorithm
Rest of the Interpolation algorithm is same except the above partition logic.

Step1: In a loop, calculate the value of “pos” using the probe position formula.
Step2: If it is a match, return the index of the item, and exit.
Step3: If the item is less than arr[pos], calculate the probe position of the left sub-array. 
Otherwise calculate the same in the right sub-array.
Step4: Repeat until a match is found or the sub-array reduces to zero.
'''

def interpolationSearch(sorted_list, to_find):

    low = 0
    high = len(sorted_list) - 1

    while sorted_list[low] <= to_find and sorted_list[high] >= to_find:
        mid = (low + ((to_find - sorted_list[low]) * (high - low)) \
                / (sorted_list[high] - sorted_list[low]))

        if sorted_list[mid] < to_find:
            low = mid + 1
        elif sorted_list[mid] < to_find:
            high = mid - 1
        else:
            return mid

    if sorted_list[low] == to_find:
        return low

    return None

'''
index: 5
index: None
'''
if __name__ == "__main__":
    theSeq = [10, 12, 13, 16, 31, 33, 35, 42, 47] 
    target = 33
    index = interpolationSearch(theSeq, target)
    print 'index:', index

    target = 32
    index = interpolationSearch(theSeq, target)
    print 'index:', index
