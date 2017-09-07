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
        
        
'''
Solve tower of hanoi using iterative way
'''
import sys

class Peg:
    """ Stack representing one Hanoi peg. """
    def __init__(self, n=0):
        self.stack = []
        self.stack.extend(range(1,n+1))

    def count(self):
        return len(self.stack)

    def empty(self):
        return self.count()==0

    def top(self):
        return self.stack[-1] if not self.empty() else 0

    def pop(self):
        return self.stack.pop() if not self.empty() else 0

    def push(self, disc):
        if disc < self.top():
            raise Exception("Game rules violated")
        self.stack.append(disc)

    def __repr__(self):
        return str(self.stack)

class Pegs():
    """ Class representing three Hanoi pegs. """

    def __init__(self, n, src=1, dst=3):
        self.n = n
        self.dst = dst
        self.pegs = [None] #First non-peg to make indexing start from 1
        for i in range(3):
            self.pegs.append(Peg(n if i==src-1 else 0))

    def simplemove(self, src, dst):
        disc = self.pegs[src].pop()
        print("from {} to {}.".format(src, dst))
        self.pegs[dst].push(disc)
        print(self)

    def legalmove(self, first, second):
        """Performs the only legal move between two pegs."""
        d1 = self.pegs[first].top()
        d2 = self.pegs[second].top()
        if d1 > d2:
            self.simplemove(first, second)
        else:
            self.simplemove(second, first)

    def finished(self):
        return self.pegs[self.dst].count() == self.n

    def __repr__(self):
        return str(self.pegs[1:])


def hanoj(n, src=1, dst=3, tmp=2):
    if n % 2 == 0: # Even disc flow
        flow = ((src, tmp), (src, dst), (dst, tmp))
    else: #Odd disc flow
        flow = ((src, dst), (src, tmp), (dst, tmp))

    p = Pegs(n, src)
    step = 0
    while not p.finished():
        print("Step {:03}: ".format(step+1), end="")
        p.legalmove(*flow[step % 3])
        step += 1


if __name__ == "__main__":
    hanoj(int(sys.argv[1]))
    
'''
[root@RND-SM-1-59Q tmp]# python iterHani.py 3
Step 001: from 1 to 3.
[[1, 2], [], [3]]
Step 002: from 1 to 2.
[[1], [2], [3]]
Step 003: from 3 to 2.
[[1], [2, 3], []]
Step 004: from 1 to 3.
[[], [2, 3], [1]]
Step 005: from 2 to 1.
[[3], [2], [1]]
Step 006: from 2 to 3.
[[3], [], [1, 2]]
Step 007: from 1 to 3.
[[], [], [1, 2, 3]]
'''
