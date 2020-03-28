
count = 0
arr = [2, 4, 6, 10, 12,1 ,2 ,3 ,1, 1, 1, 1, 1]


def DP( i, target):
    global arr
    if ( target == 0 ):
        global count
        count += 1
        return
    elif ( i>= len(arr)): return 0

    DP( i+1, target-arr[i])
    DP( i+1, target)

    return



if __name__ == "__main__":

    

    DP( 0, 12)
    print(count)


    