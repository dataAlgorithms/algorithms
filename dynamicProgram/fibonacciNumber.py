'''
Method 1: simple recursive program for Fibonacci numbers
'''
def fib_recursive(n):

    if n <= 1:
        return n

    return fib_recursive(n-1) + fib_recursive(n-2)

'''
Method 2: Memoization (Top Down) of dynamic programing
'''
MAX = 100
lookup = [None] * MAX

# Function for nth Fibonacci number (Memoization)
def fib_memo(n):

    if lookup[n] is None:
        if n <= 1:
            lookup[n] = n
        else:
            lookup[n] = fib_memo(n-1) + fib_memo(n-2)

    return lookup[n]

'''
Method 3: Tabulation (Bottom Up) of dynamic programing
'''
def fib_tabu(n):

    if n <= 1:
        return n

    f = [0] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]

'''
Use simple recursive program!
-1
Seconds: 0.0
0
Seconds: 0.0
1
Seconds: 0.0
1
Seconds: 0.0
21
Seconds: 0.0
832040
Seconds: 0.286000013351

Use memoization of dynamic programing
-1
Seconds: 0.0
0
Seconds: 0.0
1
Seconds: 0.0
1
Seconds: 0.0
21
Seconds: 0.0
832040
Seconds: 0.0

Use tabulation of dynamic programing!
-1
Seconds: 0.0
0
Seconds: 0.000999927520752
1
Seconds: 0.0
1
Seconds: 0.0
21
Seconds: 0.0
832040
Seconds: 0.0
'''
if __name__ == "__main__":
    import time

    print 'Use simple recursive program!'
    for n in [-1, 0, 1, 2, 8, 30]:
        starttime = time.time()
        print fib_recursive(n)
        print 'Seconds:', time.time() - starttime

    print '\nUse memoization of dynamic programing!'
    for n in [-1, 0, 1, 2, 8, 30]:
        starttime = time.time()
        print fib_memo(n)
        print 'Seconds:', time.time() - starttime

    print '\nUse tabulation of dynamic programing!'
    for n in [-1, 0, 1, 2, 8, 30]:
        starttime = time.time()
        print fib_tabu(n)
        print 'Seconds:', time.time() - starttime
