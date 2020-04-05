def isHappy(n):

    sum = 0
    loopArr=[]
    numArr = []

    while (sum != 1):

        print(loopArr, n)
        
        

        sum = 0
        numArr = []
        while(n > 0):
            #print(n % 10, n//10, numArr, sum)
            numArr.append(n % 10)
            
            n = n//10

        for i in numArr:
            
            sum += i*i
            
        #print(sum);
        if( sum in loopArr): return False

        n = sum
        loopArr.append(sum)
        
    return True


if __name__ == "__main__":

    print(isHappy(9))
