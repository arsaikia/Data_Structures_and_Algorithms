# Naive Fibonacci
# O(2^N) Time || O(N) Space
def Fib( n ):

    if n ==1: return 0
    elif n == 2: return 1
    else:
        return Fib(n-1) +  Fib(n-2)

# Memoized Fibonnacci
# O(N) Time || O(N) Space
def getMemoizedFib( n, memoize ={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getMemoizedFib(n-1, memoize), getMemoizedFib(n-2, memoize)
        return memoize[n]

# Iterative Fibonacci || Memoized solution
# O(N) Time || O(1) Space
def iterativeFib( n ):
    lastTwo = [0, 1]
    counter= 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0], lastTwo[1] = lastTwo[1], nextFib
        counter += 1
    return lastTwo[1] if n>1 else lastTwo[0]