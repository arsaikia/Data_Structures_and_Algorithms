# Fibonnaci
import time as t
# Naive

def Naivefib( n ):
    if n == 1: return 0
    elif n == 2: return 1
    else: return Naivefib(n-1) + Naivefib(n-1)

def Memoizedfib( n , memo={1:0, 2: 1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = Memoizedfib(n-1, memo) + Memoizedfib(n-2, memo)
        return memo[n]

def BottomUpFib( n ):
    firstTwo = [0, 1]
    counter = 3
    while counter < n:
        value = firstTwo[0] + firstTwo[1]
        firstTwo[0], firstTwo[1] = firstTwo[1], value
        counter += 1
    return firstTwo[1] if n>1 else firstTwo[0]

start = t.time()
val = Naivefib(20)
end = t.time()
print(f'Naive Fib of 5 is {val} which takes {end-start} seconds!')
     