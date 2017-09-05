'''
Solve tower of hanoi using recursive way
'''

def towerOfHanoiUsingRecur(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print "Move disk 1 from rod", from_rod, "to rod", to_rod
        return

    towerOfHanoiUsingRecur(n-1, from_rod, aux_rod, to_rod)
    print "Move disk", n, "from rod", from_rod, "to rod", to_rod
    towerOfHanoiUsingRecur(n-1, aux_rod, to_rod, from_rod)

'''
[root@1 scripts]# python tower.py 
2 disks
Move disk 1 from rod A to rod B
Move disk 2 from rod A to rod C
Move disk 1 from rod B to rod C
-------------------
3 disks
Move disk 1 from rod A to rod C
Move disk 2 from rod A to rod B
Move disk 1 from rod C to rod B
Move disk 3 from rod A to rod C
Move disk 1 from rod B to rod A
Move disk 2 from rod B to rod C
Move disk 1 from rod A to rod C
-------------------
4 disks
Move disk 1 from rod A to rod B
Move disk 2 from rod A to rod C
Move disk 1 from rod B to rod C
Move disk 3 from rod A to rod B
Move disk 1 from rod C to rod A
Move disk 2 from rod C to rod B
Move disk 1 from rod A to rod B
Move disk 4 from rod A to rod C
Move disk 1 from rod B to rod C
Move disk 2 from rod B to rod A
Move disk 1 from rod C to rod A
Move disk 3 from rod B to rod C
Move disk 1 from rod A to rod B
Move disk 2 from rod A to rod C
Move disk 1 from rod B to rod C
-------------------
'''
if __name__ == "__main__":
    for n in [2, 3, 4]:
        print '%d disks' % n
        towerOfHanoiUsingRecur(n, 'A', 'C', 'B')
        print '-------------------'
        
        
