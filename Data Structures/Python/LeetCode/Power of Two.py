import math
def powerOfTwo( n: int) -> bool:
    return math.log2(n)%1 == 0.0 if n>0 else False

array = [-20, 0, 1, 2, 4, 16, 512, 99, 1024, 1025]

for each in array:
    print(powerOfTwo(each))

