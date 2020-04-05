def isHappy(n):

    sum = 0
    loopArr=[]
    numArr = []

    while (sum != 1):
        sum = 0
        numArr = []
        while(n > 0):
            numArr.append(n % 10)
            n = n//10
        for i in numArr:   
            sum += i*i 
        if( sum in loopArr): return False
        n = sum
        loopArr.append(sum)
    return True


if __name__ == "__main__":

    print(isHappy(9))
