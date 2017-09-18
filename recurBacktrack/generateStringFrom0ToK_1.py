'''
Generate all the strings of length n drawn from 0..k-1
'''
def kString(aList, n, k):

    if n < 1:
        print(aList)
    else:
        for j in range(0, k):
            aList[n -1] = j
            kString(aList, n-1, k)

if __name__ == "__main__":
    aList = [1, 1, 1]

    for i in [1, 2, 3]:
        kString(aList, len(aList), i)
        print("\n")

'''
[0, 0, 0]


[0, 0, 0]
[1, 0, 0]
[0, 1, 0]
[1, 1, 0]
[0, 0, 1]
[1, 0, 1]
[0, 1, 1]
[1, 1, 1]


[0, 0, 0]
[1, 0, 0]
[2, 0, 0]
[0, 1, 0]
[1, 1, 0]
[2, 1, 0]
[0, 2, 0]
[1, 2, 0]
[2, 2, 0]
[0, 0, 1]
[1, 0, 1]
[2, 0, 1]
[0, 1, 1]
[1, 1, 1]
[2, 1, 1]
[0, 2, 1]
[1, 2, 1]
[2, 2, 1]
[0, 0, 2]
[1, 0, 2]
[2, 0, 2]
[0, 1, 2]
[1, 1, 2]
[2, 1, 2]
[0, 2, 2]
[1, 2, 2]
[2, 2, 2]
'''
